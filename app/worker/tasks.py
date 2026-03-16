import asyncio

from app.worker.celery_app import app

from app.services.price_service import PriceService
from app.clients.deribit_client import DeribitClient
from app.repositories.price_repo import PriceRepo
from app.core.database import async_session_maker

async def run_price_update():
    # Создание экземпляра клиента для запросов к бирже
    client = DeribitClient()

    # Использование асинхронной сессии для работы с репозиторием и сервисом
    async with async_session_maker() as session:
        repo = PriceRepo(session)
        service = PriceService(repo, client)

        # Выполнение основного метода получения и сохранения цен
        await service.fetch_save_price()

@app.task(name='get_ticker_price')
def get_price():

    # Запуск асинхронного процесса внутри синхронной задачи Celery
    asyncio.run(run_price_update())
    return True
