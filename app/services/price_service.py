import time
import logging

from app.clients.deribit_client import DeribitClient
from app.repositories.price_repo import PriceRepo
from app.schemas.price import PriceCreate

logger = logging.getLogger(__name__)

class PriceService:
    def __init__(self, repo: PriceRepo, client: DeribitClient):
        self.repo = repo
        self.client = client
    
    async def fetch_save_price(self):
        """
        Метод запрашивает цены для нужных тикеров и сохраняет их в БД.
        """
        tickers = ["btc_usd", "eth_usd"] # Нужные тикеры

        for ticker in tickers:

            price_value = await self.client.get_price(ticker) # Получение цены

            if price_value is not None:
                # Валидация данных 
                price_data = PriceCreate(
                    ticker = ticker,
                    price = price_value,
                    timestamp = int(time.time())
                )
                # Сохранение в БД
                await self.repo.save_price(price_data)
                logger.info(f"Сохранена цена для {ticker}: {price_value}")
            else:
                logger.info(f"Нет данных для {ticker}")