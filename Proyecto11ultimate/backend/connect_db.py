import reflex as rx
from sqlmodel import create_engine

def connect():
     engine = create_engine("sqlite:///Productos.db")
     return engine










