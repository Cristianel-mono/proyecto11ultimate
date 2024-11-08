import reflex as rx
from sqlmodel import Field
class Rollo(rx.Model, table=True):
    Ancho: int
    Calibre: str
    Color: str
    Grupo: str
    Largo: int
    Material: str
    PesoPorRollo:str
    UnidadesCalibre:str
    UnidadesLargo:str
    unidadesAncho:str
    codigoSiigo:int = Field(default=None, primary_key=True)