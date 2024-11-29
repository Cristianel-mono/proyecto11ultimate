import reflex as rx

def crear_select(
    label: str,
    placeholder: str,
    name: str,
    options: list[str],
    is_visible: bool,  # Parámetro de visibilidad
    default_value: str = "",  # Valor predeterminado
) -> rx.Component:
    return rx.cond(
        is_visible,  # Condición para mostrar el componente
        rx.form.field(
            rx.flex(
                rx.hstack(
                    rx.form.label(label, style={"font-size": "15px", "margin-bottom": "6px"}),  # Etiqueta
                     align="center",
                     spacing="2",
                ),
                rx.select(
                    placeholder=placeholder,
                    items=options,
                    value=default_value,
                     style={
                         "height": "40px",  # Altura consistente
                         "padding": "8px",  # Espaciado interno
                         "font-size": "14px",  # Tamaño de fuente uniforme
                         "border-radius": "4px",  # Bordes redondeados
                         "border": "1px solid #ccc",  # Borde estándar
                         "box-shadow": "none",  # Evitar sombra resaltada
                         "outline": "none",  # Evitar foco adicional
                         "background-color": "white",  # Fondo estándar
                     },
                    
                ),
                 direction="column",
                 spacing="1",
            ),
              name=name,
             width="100%",
        ),
                 rx.fragment(),    # Componente vacío si no es visible
            )
            
            