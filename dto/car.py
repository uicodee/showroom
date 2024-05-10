from pydantic import BaseModel
from .types import CarTypes


class Car(BaseModel):

    id: int
    name: str
    category: str
    year: int
    price: float
    type: CarTypes

    class Config:
        orm_mode = True
