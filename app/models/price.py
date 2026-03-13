from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Price(Base):
    __tablename__ = "crypto_prices"

    # Суррогатный первичный ключ
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    ticker: Mapped[str] = mapped_column(String(10), index = True)

    price: Mapped[float]

    timestamp: Mapped[int] = mapped_column(index=True)