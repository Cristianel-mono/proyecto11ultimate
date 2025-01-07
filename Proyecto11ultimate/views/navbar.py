import reflex as rx

def navbar():
    return rx.flex(
        # Logo e Identidad
        rx.badge(
            rx.icon(tag="table-2", size=28),
            rx.heading("Provispol S.A", size="6"),
            color_scheme="blue",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.spacer(),
        # Botones de navegación y modo oscuro
        rx.hstack(
            rx.link(
                rx.button(
                    "Productos Eliminados",
                    color_scheme="blue",
                    variant="outline",
                    size="3",
                ),
                href="/productos-eliminados",  # Redirige a la página de productos eliminados
                underline="none",
            ),
            rx.link(
                rx.button(
                    "Registro Productos",
                    color_scheme="green",
                    variant="solid",
                    size="3",
                ),
                href="/",  # Redirige a la página principal
                underline="none",
            ),
            rx.color_mode.button(),
            align="center",
            spacing="3",
        ),
        # Espaciado y diseño
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="2em",
        padding_x=["1em", "1em", "2em"],
        background_color=rx.color("gray", 1),
        border_bottom="1px solid #ccc",
        position="sticky",
        z_index="5",
    )
