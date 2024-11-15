import reflex as rx
from sqlmodel import Field
#Rollo es el nombre de la tabla de mi base de datos
class Rollo(rx.Model, table=True):
     Ancho: int
     Calibre: int
     Color: str
     Grupo: str
     Largo: int
     fecha: str
     Material: str
     PesoPorRollo:int
     UnidadesCalibre:str
     UnidadesLargo:str
     unidadesAncho:str
     Codigo_Siigo:int = Field(default=None, primary_key=True)

     