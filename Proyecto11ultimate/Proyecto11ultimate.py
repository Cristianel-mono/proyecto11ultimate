import reflex as rx
from .views.navbar import navbar
from .views.table import main_table
from .ProductosEliminados import ProductosEliminados
from .backend.backend import States_pagina


@rx.page()
def index() -> rx.Component:
    print("ejecutando el index")
    return rx.vstack(
        navbar(),
        rx.box(
            main_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )


app = rx.App(
    theme=rx.theme(
         has_background=True, radius="large", accent_color="blue"
    ),
)

app.add_page(
    index,
    title="Provispol S.A",
    description="Pagina Principal",
)
app.add_page(
    ProductosEliminados,
    title='Productos eliminados',
    description='se muestran los productos eliminados',
)
