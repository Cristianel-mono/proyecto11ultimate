import reflex as rx

def crear_select(label, placeholder, name, items, value, required, is_visible=True, on_change= None):
    return rx.cond(
        is_visible,
        rx.flex(
            rx.text(label, font_weight="bold", margin_bottom="0.5em"),
            rx.select(
                items=items,
                placeholder=placeholder,
                name=name,
                value=value,
                required=required,
                on_change=on_change,
                width="100%",
            ),
            width="100%",
            justify="center",
            flex_wrap="nowrap",
            direction="column",
        )
    )
