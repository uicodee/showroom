from fastapi import FastAPI

from .car import router as car_router


def setup(app: FastAPI):
    app.include_router(
        router=car_router,
        tags=["Car"],
    )
