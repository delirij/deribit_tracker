from pydantic import BaseModel, ConfigDict


# Базовая схема с общими полями для всех операций
class PriceBase(BaseModel):
    ticker: str
    price: float
    timestamp: int


# Схема для валидации данных при создании новой записи
class PriceCreate(PriceBase):
    pass


# Схема для формирования ответа API
class PriceResponse(PriceBase):
    # Уникальный идентификатор из базы данных
    id: int

    # Настройка для автоматического преобразования из объектов SQLAlchemy
    model_config = ConfigDict(from_attributes=True)
