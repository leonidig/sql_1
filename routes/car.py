from app import app
from flask import render_template
from models import Car, Session
from sqlalchemy import select

@app.get("/cars_list")
def cars_list():
    context = {}
    with Session.begin() as session:
        context["items"] = session.scalars(select(Car)).all()

    return render_template("list.html", context = context)