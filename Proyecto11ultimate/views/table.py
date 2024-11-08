import reflex as rx

from Proyecto11ultimate.views.formulariosProducto import bolsa_form , rollo_form , rolloProviAgro_form , servicio_form
from ..backend.backend import States_pagina
from ..components.form_field import crear_forma
import reflex as rx
from ..backend.productos_model import Rollo 


def base_form():
    """Formulario base que muestra el formulario según el tipo de producto seleccionado."""
    
    # Opciones de tipos de productos en un radio button
    product_type_radio = rx.radio_group(
        items=["Bolsa", "Rollo", "Rollo Proviagro", "Servicio"],
        name="tipo_producto",
        on_change=States_pagina.update_selected
         
         ), 

    # Renderizado del formulario base
    return rx.fragment(
        rx.text("Creación de Referencias", weight="bold", size="2xl", margin_bottom="1em"),
        rx.text("Seleccione el tipo de producto:", weight="bold"),
        product_type_radio,
        
        # Condiciones para mostrar el formulario según el tipo seleccionado
        rx.cond(
            States_pagina.selected_product == "Bolsa",  # Usar la variable seleccionada aquí
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

        # Botones de envío y cancelar en el formulario base
        rx.hstack(
            rx.button("Cancelar", color_scheme="red"),
            rx.button("Enviar", color_scheme="blue"),
            justify="end",
            margin_top="1em",
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
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",  # Corrección en las comillas
            border_radius="25px",
        )
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
def table_producto(list_rollo: list[Rollo])-> rx.Component:#La tabla recibe una lista de usuario
    print("Datos de table_producto:", list_rollo)                                                
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                _header_cell("Grupo", "ruler"),
                _header_cell("Color", "ruler"),
                _header_cell("Calibre", "ruler"),#aca declaramos les headers
                _header_cell("Ancho", "ruler"),
                _header_cell("Largo", "ruler"),
                _header_cell("Referencia final", "ruler"),
            )
        ),
        rx.table.body(
            rx.foreach(list_rollo, row_table)#iteramos la lista de usuarios y se los pasamos
                                                #al componente row_table

        )
    )
def row_table(rollo: Rollo) -> rx.Component:
    return rx.table.row(
        rx.table.cell(rollo.Grupo),
        rx.table.cell(rollo.Color),
        rx.table.cell(rollo.Calibre),
        rx.table.cell(rollo.Ancho),
        rx.table.cell(rollo.Largo),
        rx.table.cell(
            rx.hstack(
                rx.button("Eliminar")
        )
)


    )
def main_table():
    return rx.fragment(
        rx.flex(
            add_reference_button(),
            rx.spacer(),
            rx.icon(
                "arrow-down-a-z",
                size=28,
                stroke_width=1.5,
                cursor="pointer",
            ),
            rx.select(
                ["Tipo de Producto", "color", "calibre", "referencia"],
                placeholder="Buscar Referencia por",
                size="3",
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Buscar aquí",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
            table_producto(States_pagina.rollo),#traemos los usuarios de la clase state 
            variant="surface",
            size="3",
            width="100%",
        ),
    