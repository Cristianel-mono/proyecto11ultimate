import reflex as rx
from sqlmodel import Session, select
from ..backend.connect_db import connect
from ..backend.productos_model import Rollo


def select_rollo():
     engine = connect()
     with Session(engine) as session:
         query = select(Rollo)
         results = session.exec(query).all()
         print("Resultados de la consulta:", results)  # Agregar un print para depurar
     return results
