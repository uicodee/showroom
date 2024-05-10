from fastapi import FastAPI
import uvicorn as uvicorn
import controllers
from database import models
from database.database import engine

models.Base.metadata.create_all(bind=engine)


def main() -> FastAPI:
    app = FastAPI(
        title="Showroom API",
        description="Showroom API",
        version="1.0.0"
    )
    controllers.setup(app)
    return app


if __name__ == '__main__':
    uvicorn.run(
        "main:main",
        port=8000,
        reload=True
    )
