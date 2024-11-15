import reflex as rx
from sqlmodel import create_engine

def connect():
     engine = create_engine("sqlite:////home/systemas/Documentos/Proyecto11ultimate/Productos.db")
     return engine










