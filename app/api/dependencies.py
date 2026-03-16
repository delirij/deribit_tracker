from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_maker
from app.repositories.price_repo import PriceRepo

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Открывает сессию при запросе и автоматически закрывает её после ответа пользователю
    """
    async with async_session_maker() as session:
        yield session

def get_price_repo(session: AsyncSession = Depends(get_db)) -> PriceRepo:
    """
    Автоматически берет сессию из get_db и создает готовый к работе репозиторий 
    """
    return PriceRepo(session)