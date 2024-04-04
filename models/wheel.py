from . import Car
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Wheel(Car):
    __tablename__ = "wheel"
    # id: Mapped[int] = mapped_column(primary_key=True)
    # brand: Mapped[str]
    # model_name: Mapped[str]
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
    car: Mapped[Car] = relationship(back_populates="wheels")