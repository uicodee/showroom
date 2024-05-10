from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schems
from database import crud
from dependencies.database import get_db

router = APIRouter()


@router.get("/")
async def get_cars(
        db: Session = Depends(get_db)
):
    return crud.get_cars(db)


@router.post("/new")
async def create_car(
        car: schems.Car,
        db: Session = Depends(get_db)
):
    return crud.create_car(db, car)


@router.put("/edit")
async def update_car(
        car: schems.EditCar,
        db: Session = Depends(get_db)
):
    return crud.edit_car(db, car)


# /delete?car_id=1221323
@router.delete("/delete")
async def delete_car(car_id: int, db: Session = Depends(get_db)):
    return crud.delete_car(db, car_id)
