import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime
from ..backend.productos_model import Rollo
from ..backend.metodosdb import select_rollo


class States_pagina(rx.State):
    rollo: list[Rollo] = []  # Inicializamos la lista vacía para evitar errores
    
    selected_product: str = "Bolsa"  # Producto seleccionado en la interfaz.

    

    def update_selected(self, selected_product):
        self.selected_product = selected_product
    
    async def get_all_products(self):
        async with self:
            self.rollo = select_rollo()