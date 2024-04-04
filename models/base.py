from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from __future__ import annotations
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship



engine = create_engine("sqlite://my_db.db", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    # id: Mapped[int] = mapped_column(primary_key=True)
    # brand: Mapped[str]
    # model_name: Mapped[str]
    # # wheels: Mapped[List["Wheel"]] = relationship(back_populates="car")
    # # __tablename__ = Base.tablename()
    pass


def up():
    Base.metadata.create_all(bind=engine)

def down():
    Base.metadata.drop_all(bind=engine)