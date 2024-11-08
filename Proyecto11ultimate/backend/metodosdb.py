import reflex as rx
from ..backend.productos_model import Rollo
from ..backend.connect_db import connect
from sqlmodel import Session, select

def select_rollo():
    engine = connect()
    with Session(engine) as session: #aca lo que hace que cuando terminamos la operacion 
         query = select(Rollo)                               #cierra la sesion
         return session.exec(query).all() #aca devuelve una lista 











# def get_rollos():
#     # Obtiene la colección "productos" y accede al documento "Rollo"
#     print("Intentando acceder a la colección 'productos' y al documento 'Rollo'...")  # Mensaje de depuración
#     productos_ref = db.collection('productos')  # Referencia a la colección 'productos'
#     rollo_ref = productos_ref.document('Rollo')  # Referencia al documento 'Rollo' dentro de 'productos'
    
#     print("Accediendo al documento 'Rollo'...")  # Mensaje de depuración
#     doc = rollo_ref.get()  # Obtiene el documento
    
#     if doc.exists:
#         print("Documento encontrado. Datos:", doc.to_dict())  # Muestra los datos si el documento existe
#         return doc.to_dict()  # Devuelve los datos del documento como un diccionario
#     else:
#         print("No se encontró el documento 'Rollo'.")  # Mensaje de depuración si el documento no existe
#         return []  # Si no existe, retorna un arreglo vacío
