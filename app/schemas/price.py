from pydantic import BaseModel, ConfigDict


class PriceBase(BaseModel):
    ticker: str
    price: float
    timestamp: int


class PriceCreate(PriceBase):
    pass


class PriceResponse(PriceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
