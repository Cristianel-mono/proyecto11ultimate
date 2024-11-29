import reflex as rx
from Proyecto11ultimate.components.crear_select import crear_select
from Proyecto11ultimate.components.form_field import crear_forma
from ..backend.backend import States_pagina
from ..views.Listados import Grupo , Material, Color, Tipo_Producto, Grupos_por_Tipo_Producto,Unidades_Ancho,Unidades_Largo,Unidades_Calibre, Tipo_Bobinado, Acabado, Tratado, Numero_Bobinado
from reflex.components.radix.themes.components.select import SelectItem


# def ocultar_mostrar(label: str, field_name: str, field_component: rx.Component) -> rx.Component:
#     

#     checkbox = rx.checkbox(
#         label=f"¿Desea ingresar {label}?",
#         name=f"{field_name}_option",
#         on_change=lambda value: States_pagina.set_checkbox_state(field_name, value),
#     )

#     # Muestra el campo solo si el estado específico de la checkbox está activado
#     return rx.vstack(
#         checkbox,
#         rx.cond(States_pagina.get_checkbox_state(field_name), field_component),
  #  ocultar_mostrar("Fuelle Lateral", "fulleL", form_field("Fuelle Lateral", "Ingrese el fuelle Lateral", "number", "fuelle", "ruler")),
        # ocultar_mostrar("Fuelle fondo", "fuelleF", form_field("Fuelle Fondo", "Ingrese el fuelle de Fondo", "number", "fuelle", "ruler")),
        # ocultar_mostrar("Calibre", "calibre", form_field("Calibre", "Ingrese el calibre (mm)", "number", "calibre", "ruler")),
        # ocultar_mostrar("Referencia", "referencia", form_field("Referencia", "Ingrese la referencia de la bolsa","text", "referencia", "ruler")),

#     )

# def create_switch(cookie_type: str):
#     return rx.flex(
#         rx.text(
#             cookie_type.capitalize(),
#             as_="div",
#             size="2",
#             margin_bottom="4px",
#             weight="bold",
#         ),
#         rx.switch(
#             name=cookie_type,
#             on_change=lambda checked: States_pagina.update_cookies(
#                 cookie_type,
#                 False,
#             ),
#         ),
#         direction="row",
#         justify="between",
#     )

# Función para el formulario de producto Bolsa 
def bolsa_form():
    return rx.form(
        rx.vstack(
            rx.text("Creación de referencia para Bolsas", weight="bold", size="xl"),
            rx.text(
                "Por favor complete los campos opcionales y seleccione las características del producto",
                italic=True,
                margin_bottom="1em",
            ),
            rx.text("Selecciona los parámetros opcionales que desea agregar a su bolsa", weight="bold"),
            
            # Checkbox para parámetros opcionales
            # rx.hstack(
            #      rx.heading(States_pagina.checkboxes),
            #      rx.checkbox(
            #     name="Fuelle_L",
            #     label="Desea agregar Fuelle Lateral",
            #     checked=States_pagina.checkboxes["Fuelle Lateral"],  
            #     on_change=lambda checked: States_pagina.set_checkboxes("Fuelle Lateral", checked),  
            # ),
            # rx.text("Fuelle Lateral"),
            # ),
        #     rx.hstack(
            
        #     rx.checkbox(
        #     name="Calibre",
        #     label="Desea agregar Calibre",
        #     on_change= States_pagina.update_checkbox("Calibre", True),
        #    ), 
        #    rx.text("Calibre") 
        #    ),

          
            
           
            
            # rx.checkbox(
            #     name="Fuelle_Fondo",
            #     label="Desea agregar Fuelle Fondo",
            #     checked=States_pagina.checkboxes["Fuelle Fondo"],
            #     on_change=lambda checked: States_pagina.set_checkboxes("Fuelle Fondo", checked),
            # ),
            # rx.checkbox(
            #     name="Referencia",
            #     label="Desea agregar Referencia",
            #     checked=States_pagina.checkboxes["Referencia"],
            #     on_change=lambda checked: States_pagina.set_checkboxes("Referencia", checked),
            # ),

            # Condiciones para mostrar los campos según el estado de las checkboxes
            # rx.cond(
            #     States_pagina.checkboxes == {"Fulle Lateral"},
            #     form_field("Fuelle Lateral", "Ingrese el fuelle lateral", "number", "fuelle", "ruler")
            # ),
            # rx.cond(
            #     States_pagina.checkboxes["Fuelle Fondo"],
            #     form_field("Fuelle Fondo", "Ingrese el fuelle de fondo", "number", "fuelle_fondo", "ruler")
            # ),
            # rx.cond(
            # States_pagina.checkbox_states["Calibre"],  # Esto revisará si es True directamente
            # crear_forma("Calibre", "Ingrese el calibre (mm)", "number", "calibre", "ruler")
            # ),
            # rx.cond(
            #     States_pagina.checkboxes["Referencia"],
            #     form_field("Referencia", "Ingrese la referencia de la bolsa", "text", "referencia", "ruler")
            # ),

              # Selección de material
              rx.text("Selecciona el material de su Bolsa"),
              rx.select(
                Material,
                placeholder="Elige el material",
                name="material",
                required=True,
            ),
            # Selección de color
            # rx.text("Seleccione el color"),
            # rx.select(
            #     [Color],
            #     placeholder="Elige el color",
            #     name="color",
            #     required=True,  
            # ),

            # Campos adicionales
            crear_forma("Ancho (cm)", "Ingrese el Ancho", "number", "ancho", "ruler"),
            crear_forma("Largo (cm)", "Ingrese el Largo", "number", "largo", "ruler")
        )
    )

# Convertir claves y grupos a una lista de diccionarios
# Opciones iniciales para el selector de tipo de producto

items_tipo_producto: list = list(Grupos_por_Tipo_Producto.keys()),
items_grupo = States_pagina.grupos_disponibles  # Sin transformar a diccionarios
# is_visible_numero_bobinado = States_pagina.campos_visibles["numero_bobinado"],
# def mostrar_ocultar(campo, is_visible):
#     return rx.cond(
#        is_visible,
#        campo,
#        None
#     )
# numero_bobinado = rx.select(
#                 Numero_Bobinado,
#                 placeholder="Número de Bobinado",
#                 name="Número Bobinado",
#                 required=False,
                
#             ),

  
def rollo_form():
    return rx.form(
        rx.vstack(
            # Título del formulario
            rx.text("Creación de referencia para Rollos", weight="bold", size="xl"),
            rx.text(
                "Por favor complete los campos opcionales y seleccione las características del producto",
                italic=True,
                margin_bottom="1em",
            ),
            rx.text("Selecciona los parámetros que desea agregar:", weight="bold"),
            
            # Selección del Tipo de Producto
            rx.text("Seleccione el Tipo de Producto"),
            rx.select(
                Tipo_Producto,  # Opciones del tipo de producto
                placeholder="Elija el Tipo de Producto",
                name="Tipo_Producto",
                required=True,
                on_change=States_pagina.actualizar_tipo_producto,  # Actualizar dinámicamente
            ),
            
            # Selección de Grupo
            rx.text("Seleccione el Grupo"),
            rx.select(
                items=items_grupo,
                placeholder="Elija el Grupo",
                name="Grupo",
                required=True,
                on_change=States_pagina.actualizar_grupo,
            ),
            
            # Selección de materiales
            crear_select(
                "Material 1",
                "Ingrese el Material 1",
                "Material",
                Material,
                is_visible=States_pagina.campos_visibles["Material_1"],
                default_value=States_pagina.valores_campos["Material_1"]

            ) ,
            
            crear_select(
                "Material 2",
                "Ingrese el material 2",
                "",
                Material,
                is_visible=States_pagina.campos_visibles["Material_2"]
            ),
            crear_select(
                "Material 3",
                "Ingrese el material 3",
                "",
                Material,
                is_visible=States_pagina.campos_visibles["Material_3"]
            ),
            
            # Selección de color 
            crear_select(
                "Color",
                "Ingrese el Color",
                "Color",
                Color,
                is_visible=States_pagina.campos_visibles["Color"],
                default_value=States_pagina.valores_campos["Color"]

            ) ,
            
            # Campos de dimensiones
            rx.flex(
                 crear_forma("Ancho", "Ingrese el Ancho", "number", "Ancho", "ruler", is_visible=True),
            
                crear_select(
                     "",
                     "Unidades Ancho",
                     "Unidades_Ancho",
                     Unidades_Ancho,
                     is_visible=True,
                     default_value=States_pagina.valores_campos["Unidades_Ancho"],
                
                    ),  

            
                width="100%",
                justify="center",
                flex_wrap="nowrap",
                direction="column",
            ),
            rx.flex(
                crear_forma("Largo", "Ingrese el Largo", "number", "Largo", "ruler", is_visible=True),
                 crear_select(
                     "",
                     "unidades Largo",
                     "Unidades_Largo",
                     Unidades_Largo,
                     is_visible=True,
                     default_value=States_pagina.valores_campos["Unidades_Largo"],
                
                    ),  
    
                
                width="100%",
                justify="center",
                flex_wrap="nowrap",
                direction="column",
           
            ),
            
           
               
               rx.flex(
                      crear_forma("Calibre", "Calibre", "number", "Calibre", "ruler", is_visible=True),

                      crear_select(
                     "",
                     "Unidades Calibre",
                     "Unidades_Calibre",
                     Unidades_Calibre,
                     is_visible=True,
                     default_value=States_pagina.valores_campos["Unidades_Calibre"],
                
                    ),    
                   
                width="100%",
                justify="center",
                flex_wrap="nowrap",
                direction="column",
            ),
            
            # Peso
            crear_forma("Peso por Estructura", "Ingrese el Peso", "number", "Peso_Estructura", "weight", is_visible= States_pagina.campos_visibles["Peso_Estructura"]),
            
            # Tipo y Número de Bobinado
            rx.text("Tipo de Bobinado"),
            rx.select(
                Tipo_Bobinado,
                placeholder="Tipo de Bobinado",
                name="Tipo Bobinado",
                required=True,
            ),
            # numero_bobinado =
            crear_select(
                "Numero de Bobinado",
                "Ingrese el numero de bobinado",
                "Numero_Bobinado",
                Numero_Bobinado,
                is_visible=States_pagina.campos_visibles["Numero_Bobinado"],
            ) ,
            
            

            crear_forma(
                "Peso Rollo",
                "Ingrese el peso por Rollo",
                "str",
                "Peso Rollo",
                "ruler",
                is_visible = True,
            ),
            
            # Fuelle Izquierdo y Derecho
            crear_forma(
                "Fuelle Izquierdo",
                "Ingrese el Fuelle Izquierdo",
                "number",
                "Fuelle Izquierdo",
                "ruler",
                is_visible= States_pagina.campos_visibles["Fuelle_izquierdo"],
            ),
            crear_forma(
                "Fuelle Derecho",
                "Ingrese el Fuelle Derecho",
                "number",
                "Fuelle Derecho",
                "ruler",
                is_visible=States_pagina.campos_visibles["Fuelle_derecho"],
            ),
            
            # Acabado
             crear_select(
                "Acabado",
                "Ingrese el tipo de Acabado",
                "Acabado",
                Acabado,
                is_visible=States_pagina.campos_visibles["Acabado"]
            ) ,
            
            # Tratado
              crear_select(
                "Tratado",
                "Ingrese el tipo de tratado",
                "tratado",
                Tratado,
                is_visible=States_pagina.campos_visibles["Tratado"]
            ),
            
            # Código Siigo
            crear_forma("Código Siigo", "Ingrese el Código Siigo", "number", "Codigo_Siigo", "ruler", is_visible= True),
            
            # Botones de acción
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", variant="soft", color_scheme="gray"),
                ),
                rx.form.submit(
                    rx.dialog.close(rx.button("Agregar Referencia")),
                    as_child=True,
                ),
                padding_top="2em",
                spacing="3",
                mt="4",
                justify="end",
            ),
        ),
        on_submit=States_pagina.agregarProducto_to_db,
        reset_on_submit=False,
        width="100%",
        direction="column",
        spacing="4",
        max_width="450px",
        padding="1.5em",
        border_radius="25px",
    )

def rolloProviAgro_form():
    return rx.form(
        rx.vstack(
         rx.text("Creacion de referencia para Rollos Proviagro", weight="bold", size="xl"),
        rx.text(
            "Por favor complete los campos opcionales y selecione las caracteristicas del producto",
            italic=True,
            margin_botton="1em",
        ),

        rx.text("Seleccione los parámetros del Rollo de la Línea Industrial", weight="bold"),
        rx.select(
            ["ROLLO PROVIAGRO ENERGY", "ROLLO PROVIAGRO BLACK", "ROLLO PROVIAGRO LUMINANCE", "ROLLO PROVIAGRO SPECTRUM"],
            placeholder="Elija el tipo de rollo",
            name="tipoRollo",
            required=True,
        ),
        rx.text("Seleccione el color"),
        rx.select(
            ["Amarillo", "Azul", "Blanco-Negro", "Blanco", "Naranja", "Negro", "Rojo",
             "Transparente", "Verde", "Blanco-Blanco", "Gris", "Plata-Negro"],
            placeholder="Elija el color",
            name="color_R",
            required=True,  
        ),
        crear_forma("Ancho (cm)", "Ingrese el Ancho", "number", "anchoRolloProviagro", "ruler"),
        crear_forma("Calibre (mm)", "Ingrese el Calibre", "number", "calibreRolloProviagro", "ruler"),
        crear_forma("Largo (cm)", "Ingrese el Largo", "number", "largo", "ruler"),
        rx.text("Seleccione el Tipo de Bobinado"),
        rx.select(
            ["Tubular", "Semitubular", "Lámina", "Lámina doble"],
            placeholder="Elija el tipo de bobinado",
            name="bobinadoRolloProviagro",
            required=True,
        ),
    )
    )


def servicio_form():
    return rx.form(
    rx.vstack(
         rx.text("Creacion de referencia para Servicios", weight="bold", size="xl"),
        rx.text(
            "Por favor complete los campos opcionales y selecione las caracteristicas del producto",
            italic=True,
            margin_botton="1em",
        ),

        rx.text("Seleccione el tipo de servicio que desea crear"),
        rx.select(
            ["Co-extrusión", "Corte", "Extrusión", "Maquila enfuellado", 
             "Impresión", "Laminación", "Peletizado", "Precorte", "Maquila precorte", 
             "Refilado", "Sellado", "Troquelado"],
            name="TipoServicio",
            required=True,
        ),
        # ocultar_mostrar(
        #     label="Agregar otro servicio",
        #     field_name="TipoServicio2",
        #     field_component=rx.select(
        #         ["Co-extrusión", "Corte", "Extrusión", "Maquila enfuellado", 
        #          "Impresión", "Laminación", "Peletizado", "Precorte", "Maquila precorte", 
        #          "Refilado", "Sellado", "Troquelado"],
        #         name="TipoServicio2",
        #     )
        ),
         crear_forma("Informacion del Producto", "Ingrese la info", "text", "infoServicio", "ruler"),
    )

    
    

        
    
    