import reflex as rx

def crear_select(
    label: str,
    placeholder: str,
    name: str,
    options: list[str],
    is_visible=None,  # Parámetro de visibilidad
) -> rx.Component:
    # Usar rx.cond para manejar la visibilidad
    return rx.cond(
        is_visible,  # Condición para mostrar el componente
        rx.form.field(
            rx.flex(
                rx.hstack(
                    rx.form.label(label),  # Etiqueta del campo
                    align="center",
                    spacing="2",
                ),
                rx.select(
                    placeholder=placeholder,
                    items=options,  # Pasamos directamente las opciones como items
                ),
                direction="column",
                spacing="1",
            ),
            name=name,
            width="100%",
        ),
        rx.fragment(),  # Componente vacío si no es visible
    )
