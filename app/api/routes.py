from typing import List

from fastapi import APIRouter, Depends

from app.api.dependencies import get_price_repo
from app.repositories.price_repo import PriceRepo
from app.schemas.price import PriceResponse

# Настройка роутера для группы эндпоинтов, связанных с ценами
router = APIRouter(prefix="/prices", tags=["Prices"])


@router.get("/all", response_model=List[PriceResponse])
async def get_all_prices(
    ticker: str, # Обязательный параметр валютной пары (например, btc_usd)
    repo: PriceRepo =Depends(get_price_repo) # Инъекция репозитория для работы с БД
):
    """Возвращает всю историю изменений цены по указанному тикеру"""
    result = await repo.get_all_price(ticker)

    return result

@router.get("/latest", response_model=PriceResponse)
async def get_last_prices(
    ticker: str,
    repo: PriceRepo = Depends(get_price_repo)
):
    """Возвращает последнюю актуальную запись цены из базы данных"""
    result = await repo.last_price(ticker)

    return result


@router.get("/filter", response_model=List[PriceResponse])
async def get_price_date(
    ticker: str,
    date_from: int,
    date_to: int,
    repo: PriceRepo = Depends(get_price_repo)
):
    """Поиск цен в заданном временном диапазоне"""
    result = await repo.sort_date(ticker, date_from, date_to)

    return result
