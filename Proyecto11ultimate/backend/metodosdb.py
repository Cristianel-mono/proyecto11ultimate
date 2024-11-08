import reflex as rx
from ..backend.productos_model import Rollo
from ..backend.connect_db import connect
from sqlmodel import Session, select


def select_all():
    engine = connect()
    with Session(engine) as session: #aca lo que hace que cada vez que interactuemos con nuestra base de datos el crea un sesion y la cierra nuevamente 
        query = select(Rollo)
        return session.exec(query).all()
