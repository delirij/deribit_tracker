import time

from sqlalchemy import select, desc, and_

from app.core.database import connection
from app.models.price import Price


class PriceRepo():
    @connection
    async def save_price(self, ticker: str, price:float, session):
        new_price = Price(ticker=ticker,price=price, timestamp=int(time.time()))
        session.add(new_price)
        await session.commit()

    @connection
    async def get_all_price(self, ticker:str, session):
        query = select(Price).where(Price.ticker == ticker).order_by(desc(Price.timestamp))
        result = await session.execute(query)
        return result.scalars().all()
    
    @connection
    async def last_price(self, ticker:str, session):
        query = select(Price).where(Price.ticker == ticker).order_by(desc(Price.timestamp)).limit(1)   
        result = await session.execute(query)     
        return result.scalar_one_or_none()
    
    @connection
    async def sort_date(self, ticker: str, date_from: int, date_to: int, session):
        query = select(Price).where(
            and_(
                Price.ticker == ticker,
                Price.timestamp.between(date_from, date_to)
            )
        ).order_by(desc(Price.timestamp))
        result = await session.execute(query)
        return result.scalars().all()