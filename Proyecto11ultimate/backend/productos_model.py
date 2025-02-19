import reflex as rx
from sqlmodel import Field
from typing import Optional

#Rollo es el nombre de la tabla de mi base de datos
class Rollo(rx.Model, table=True):
     Tipo_Producto: str
     Grupo: str
     Material_1: str
     Material_2: Optional[str] = None
     Material_3: Optional[str] = None
     Color: Optional[str] = None 
     Ancho:int
     Unidades_Ancho:str
     Calibre: int
     Unidades_Calibre:str
     Largo: int
     Unidades_Largo:str
     Peso_Estructura:Optional[str] = None
     Tipo_Bobinado: Optional[str] = None
     Numero_Bobinado: Optional[str] = None
     Peso_Rollo: Optional[str] = None
     Fulle_Izquierdo: Optional[str] = None
     Fuelle_Derecho: Optional[str] = None
     Acabado: Optional[str] = None
     Tratado: Optional[str] = None
     fecha: str
     Referencia: Optional[str] = None
     Referencia_Provispol: str
     Codigo_Siigo: str = Field(primary_key=True)
     estado_eliminado: bool = Field(default=False)
     
#recordar arreglar el problema de codigo siigo que es auto incrementable