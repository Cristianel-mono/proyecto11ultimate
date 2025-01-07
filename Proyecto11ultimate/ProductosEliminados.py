import reflex as rx
from .views.navbar import navbar
from .views.table import table_productos_eliminados

@rx.page(route='/Productos_Eliminados', title='Productos Eliminados')
def ProductosEliminados() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.box(
            table_productos_eliminados(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )