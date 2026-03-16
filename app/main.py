from fastapi import FastAPI

from app.api.routes import router as price_router

# Инициализация основного экземпляра приложения FastAPI
app = FastAPI(
    title="Deribit Price Tracker",
    description="API для получения сохраненных цен btc_usd и eth_usd"
)

# Подключение роутера со всеми эндпоинтами для работы с ценами
app.include_router(price_router)