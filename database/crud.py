from sqlalchemy import update, delete
from sqlalchemy.orm import Session

import schems
from database import models


def get_cars(db: Session):
    return db.query(models.Car).all()


def create_car(db: Session, car: schems.Car):
    car = models.Car(**car.dict())
    db.add(car)
    db.commit()
    return car


def edit_car(db: Session, car: schems.EditCar):
    db.execute(
        update(models.Car).filter(models.Car.id == car.id).values(
            name=car.name,
            category=car.category,
            year=car.year,
            price=car.price,
            type=car.type
        )
    )
    db.commit()


def delete_car(db: Session, car_id: int):
    db.execute(
        delete(models.Car).filter(models.Car.id == car_id)
    )
    db.commit()