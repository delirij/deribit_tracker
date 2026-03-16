import time

from sqlalchemy import select, desc, and_

from app.models.price import Price


class PriceRepo():
    def __init__(self, session):
        self.session = session
    
    async def save_price(self, ticker: str, price:float):
        new_price = Price(ticker=ticker,price=price, timestamp=int(time.time()))
        self.session.add(new_price)
        await self.session.commit()

    async def get_all_price(self, ticker:str):
        query = select(Price).where(Price.ticker == ticker).order_by(desc(Price.timestamp))
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def last_price(self, ticker:str):
        query = select(Price).where(Price.ticker == ticker).order_by(desc(Price.timestamp)).limit(1)   
        result = await self.session.execute(query)     
        return result.scalar_one_or_none()
    
    async def sort_date(self, ticker: str, date_from: int, date_to: int):
        query = select(Price).where(
            and_(
                Price.ticker == ticker,
                Price.timestamp.between(date_from, date_to)
            )
        ).order_by(desc(Price.timestamp))
        result = await self.session.execute(query)
        return result.scalars().all()