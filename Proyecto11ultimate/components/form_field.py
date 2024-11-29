import reflex as rx

def crear_forma(
    label: str,
    placeholder: str,
    type: str,
    name: str,
    icon: str,
    default_value: str = "",
    is_visible=None,  # Puede ser un Var
) -> rx.Component:
    return rx.cond(
        is_visible,  # Condición para mostrar el componente
        rx.form.field(
            rx.flex(
                rx.hstack(
                    rx.icon(icon, size=16, stroke_width=1.5),
                    rx.form.label(label, style={"font-size": "16px", "margin-bottom": "6px"}),
                     align="center",
                     spacing="2",
                ),
                rx.form.control(
                    rx.input(
                        placeholder=placeholder,
                        type=type,
                        default_value=default_value,
                        style={
                             "height": "40px",  # Altura consistente
                             "padding": "8px",  # Espaciado interno
                             "font-size": "14px",  # Tamaño de fuente uniforme
                             "border-radius": "4px",  # Bordes redondeados
                             "border": "1px solid #ccc",  # Borde estándar
                             "box-shadow": "none",  # Evitar resaltado por sombra
                             "outline": "none",  # Evitar foco adicional
                         },
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="1",
            ),
            name=name,
            width="100%",
        ),
        rx.fragment(),  # Componente vacío si no es visible
    )

