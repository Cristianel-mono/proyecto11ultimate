import reflex as rx

from Proyecto11ultimate.views.formulariosProducto import bolsa_form , rollo_form , rolloProviAgro_form , servicio_form
from ..backend.backend import States_pagina
from ..components.form_field import crear_forma
from ..backend.productos_model import Rollo 

def base_form():
    """Formulario base que muestra el formulario según el tipo de producto seleccionado."""

    # Opciones de tipos de productos en un radio button
    product_type_radio = rx.radio_group(
        items=["Bolsa", "Rollo", "Rollo Proviagro", "Servicio"],
        name="tipo_producto",
        on_change=States_pagina.update_selected
    )

    # Renderizado del formulario base
    return rx.fragment(
        rx.text("Creación de Referencias", weight="bold", size="2xl", margin_bottom="1em"),
        rx.text("Seleccione el tipo de producto:", weight="bold"),
        product_type_radio,

        # Condiciones para mostrar el formulario según el tipo seleccionado
        rx.cond(
            States_pagina.selected_product == "Bolsa",
            bolsa_form(),
            rx.cond(
                States_pagina.selected_product == "Rollo",
                rollo_form(),
                rx.cond(
                    States_pagina.selected_product == "Rollo Proviagro",
                    rolloProviAgro_form(),
                    rx.cond(
                        States_pagina.selected_product == "Servicio",
                        servicio_form(),
                    ),
                ),
            ),
        ),

        
    )


    
def add_reference_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Crear nueva Referencia", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(  # para alinear horizontalmente
                rx.badge(
                    rx.icon(tag="file", size=34),  # Muestra el icono de documentos
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(  # para alinear verticalmente
                    rx.dialog.title(
                        "Creación de una Nueva Referencia",  # Se configura el título
                        weight="bold",
                        margin="0",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
                
            ),
            
                base_form(),  # Llama al formulario base
                
                
        ),
        max_width="450px",
        padding="1.5em",
        border=f"2px solid {rx.color('accent', 7)}",  # Corrección en las comillas
        border_radius="25px",
    )



def _header_cell(text: str, icon: str):
     return rx.table.column_header_cell(
         rx.hstack(
             rx.icon(icon, size=18),
             rx.text(text),
             align="center",
             spacing="2",
         ),
    )

def mostrar_productos(rollo:Rollo):
    """Muestra un producto en una fila de la tabla."""
    return rx.table.row(
        rx.table.cell(rollo.Grupo),
        rx.table.cell(rollo.Material),
        rx.table.cell(rollo.Color),
        rx.table.cell(rollo.Codigo_Siigo),
        rx.table.cell(rollo.fecha),
        rx.table.cell(
            rx.icon_button(
                rx.icon("trash-2", size=22),
                on_click=lambda: States_pagina.eliminar_producto(getattr(rollo, "Codigo_Siigo")),
                size="2",
                variant="solid",
                color_scheme="red",
            ),
        ),
        # Estilo aplicado al nivel de la fila
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )





def main_table():
    return rx.fragment(
        rx.flex(
            add_reference_button(),
            rx.spacer(),
            rx.cond(
                   States_pagina.order_table,
                 rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=States_pagina.alternar_orden,
                    ),
                ),
            rx.select(
                ["Codigo_Siigo", "Material", "fecha", "Grupo"],
                placeholder="Buscar valor",
                size="3",
                on_change=lambda value: States_pagina.filtrar_valores(value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Buscar aquí",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: States_pagina.filtrar_valores(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                  _header_cell("Grupo", "ruler"),
                  _header_cell("Material", "ruler"),
                  _header_cell("Color", "ruler"),
                  _header_cell("Codigo Siigo", "ruler"),
                  _header_cell("Fecha", "ruler"),
                  _header_cell("Botones Interactivos", "ruler"),
                ),
            ),
            
            rx.table.body(rx.foreach(States_pagina.rollos, mostrar_productos)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=States_pagina.cargar_productos,
        ),
    )