import pytest

# Весь файл асинхронный
pytestmark = pytest.mark.asyncio


async def test_get_all_prices_success(ac, mock_repo):
    """Проверяем получение списка цен. Добавляем id для схемы"""
    fake_data = [
        {
            "id": 1, 
            "ticker": "btc_usd", 
            "price": 60000.0, 
            "timestamp": 123456789
        }
    ]
    mock_repo.get_all_price.return_value = fake_data

    response = await ac.get("/prices/all", params={"ticker": "btc_usd"})
    
    assert response.status_code == 200
    assert response.json() == fake_data


async def test_get_latest_price_success(ac, mock_repo):
    """Проверка последней цены. Используем метод last_price"""
    fake_price = {
        "id": 1, 
        "ticker": "eth_usd", 
        "price": 3000.0, 
        "timestamp": 123456789
    }
    
    mock_repo.last_price.return_value = fake_price

    response = await ac.get("/prices/latest", params={"ticker": "eth_usd"})
    
    assert response.status_code == 200
    # Проверяем конкретное значение, чтобы убедиться, что данные прошли
    assert response.json()["price"] == 3000.0


async def test_get_latest_price_missing_ticker(ac):
    """Тест на ошибку валидации (отсутствие тикера)"""
    response = await ac.get("/prices/latest")
    assert response.status_code == 422