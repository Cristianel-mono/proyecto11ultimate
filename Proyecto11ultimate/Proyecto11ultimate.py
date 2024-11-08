import reflex as rx
from .views.navbar import navbar
from .views.table import main_table
from .backend.backend import States_pagina



def index(on_load=States_pagina.get_all_productos) -> rx.Component:
    
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
        appearance="dark", has_background=True, radius="large", accent_color="blue"
    ),
)

app.add_page(
    index,
    title="Provispol S.A",
    description="A simple app to manage customer data.",
)
