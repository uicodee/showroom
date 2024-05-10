from sqlalchemy import String, Integer, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column

import dto
from .database import Base


class Car(Base):

    __tablename__ = 'car'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    type: Mapped[dto.CarTypes] = mapped_column(Enum(dto.CarTypes))
