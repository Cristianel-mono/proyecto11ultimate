import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime
from ..backend.productos_model import Rollo
from ..backend.metodosdb import select_all

# Opciones para los tipos de producto
# Opciones para los tipos de producto con IDs únicos
    




class States_pagina(rx.State):
    rollo:list[Rollo]
    
    selected_product: str = "Bolsa"         # Producto seleccionado en la interfaz.
    @rx.background
    async def get_all_productos(self):
        async with self:
            self.rollo = select_all()

    def update_selected(self, slected_product):
        self.selected_product = slected_product
    