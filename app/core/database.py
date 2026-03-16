from sqlalchemy.orm import  DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.core.config import settings

# Асинхронный движок для работы с БД
engine = create_async_engine(
    url=f"{settings.database_url}",
    echo = True,
    poolclass = NullPool
)

# Фабрика сессий для взаимодействия с БД
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass
