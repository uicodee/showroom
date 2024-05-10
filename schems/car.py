from pydantic import BaseModel

from dto import CarTypes


class Car(BaseModel):

    name: str
    category: str
    year: int
    price: float
    type: CarTypes


class EditCar(Car):
    id: int