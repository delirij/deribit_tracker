import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.price_service import PriceService


@pytest.mark.asyncio
async def test_fetch_save_price_no_data():
    """
    Тестим сервис. Мокаем клиент и репозиторий, 
    чтобы не ходить в реальную сеть и базу
    """
    # Создаем фейковые объекты
    mock_repo = MagicMock()
    mock_client = AsyncMock()
    
    # Говорим моку вернуть None (биржа лежит)
    mock_client.get_price.return_value = None
    
    service = PriceService(repo=mock_repo, client=mock_client)
    
    # Запускаем метод
    await service.fetch_save_price()
    
    # Проверяем, что метод сохранения в базу не вызывался, раз данных нет
    mock_repo.save_price.assert_not_called()