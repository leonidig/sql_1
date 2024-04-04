from . import Base, Wheel
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Car(Base):
    __tablename__ = "car"
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str]
    model_name: Mapped[str]
    wheels: Mapped[List["Wheel"]] = relationship(back_populates="car")