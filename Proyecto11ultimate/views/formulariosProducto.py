import reflex as rx
from Proyecto11ultimate.components.crear_select import crear_select
from Proyecto11ultimate.components.crear_imput import crear_forma
from ..backend.backend import States_pagina
from ..components.CrearReferencias import  ORDEN_CAMPOS_ROLLOS
from ..views.Listados import Grupo , Material, Color, Tipo_Producto_Rollos, Grupos_por_Tipo_Producto,Unidades_Ancho,Unidades_Largo,Unidades_Calibre
from ..views.Listados import  Tipo_Bobinado, Acabado, Tratado, Numero_Bobinado, Tipos_Productos_Bolsas, Tipo_Bolsa, Tipo_Selle, Tipo_Troquel, Tipo_Solapa
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
            rx.text("Creación de referencia para Bolsas", weight="bold", size="4"),
               rx.flex(
            rx.text("Seleccione el Tipo de Producto", font_weight="bold", margin_bottom="0.5em"),
            rx.select(
                Tipos_Productos_Bolsas,  # Opciones del tipo de producto
                placeholder="Elija el Tipo de Producto",
                name="Tipo_Producto",
                required=True,
                #on_change= lambda e: States_pagina.producto_nuevo("Tipo_Producto", e),
                on_change=States_pagina.actualizar_tipo_producto,
                #on_change=lambda e:  State_Rollo.actualizar_campo("Tipo_Producto", e),
            ),
            width="100%",
            justify="center",
            flex_wrap="nowrap",
            direction="column",
        ),

        rx.flex(
            rx.text("Seleccione el Grupo", font_weight="bold", margin_bottom="0.5em"),
            rx.select(
                items=items_grupo,
                placeholder="Elija el Grupo",
                name="Grupo",
                required=True,
                on_change=States_pagina.actualizar_grupo,
            ),
            width="100%",
            justify="center",
            flex_wrap="nowrap",
            direction="column",
        ),  
              # Selección de material
               crear_select(
                "Ingrese el Material de su bolsa",
                "Ingrese el Material",
                "Material_1",
                Material,
                value=States_pagina.valores_campos["Material_1"],
                required=False,
                is_visible=True,
                #on_change=lambda e: State_Rollo.actualizar_campo("Material_1", e),
                ),
                crear_select(
                "Material 2",
                "Ingrese el Material 2",
                "Material_2",
                Material,
                States_pagina.valores_campos["Material_2"],
                required=False,
                is_visible=States_pagina.campos_visibles["Material_2"],
                on_change=lambda e: States_pagina.actualizar_campo("Material_2", e),
                ),
                crear_select(
                "Material 3",
                "Ingrese el Material 3",
                "Material_3",
                Material,
                States_pagina.valores_campos["Material_3"],
                required=False,
                is_visible=States_pagina.campos_visibles["Material_3"],
                on_change=lambda e: States_pagina.actualizar_campo("Material_3", e),
                ),
             
        
            # Campos adicionales
            crear_forma("Ancho (cm)", "Ingrese el Ancho", "number", "ancho", "ruler", is_visible=True),
            crear_select(
                    "Unidades Ancho",
                    "Ingrese las unidades",
                    "Unidades_Ancho",
                    Unidades_Ancho,
                    States_pagina.valores_campos["Unidades_Ancho"],
                    required=True,
                    #on_change=lambda e: State_Rollo.actualizar_campo("Unidades_Ancho", e),
                ),
            crear_forma("Largo (cm)", "Ingrese el Largo", "number", "largo", "ruler", is_visible=True),
            crear_select(
                    "Unidades Ancho",
                    "Ingrese las unidades",
                    "Unidades_Ancho",
                    Unidades_Ancho,
                    States_pagina.valores_campos["Unidades_Ancho"],
                    required=True,
                   #on_change=lambda e: State_Rollo.actualizar_campo("Unidades_Ancho", e),
                ),
           
                crear_forma("Calibre", "Ingrese el Calibre", "number", "Calibre", "ruler", is_visible=True,on_change=lambda e: States_pagina.actualizar_campo("Calibre", e)),
                crear_select(
                    "Unidades Calibre",
                    "Ingrese las unidades",
                    "Unidades_Calibre",
                    Unidades_Calibre,
                    States_pagina.valores_campos["Unidades_Calibre"],
                    required=True,
                    #on_change=lambda e: State_Rollo.actualizar_campo("Unidades_Calibre", e),
                   
                ),
                crear_forma("Peso por Estructura", "Ingrese el Peso", "number", "Peso_Estructura", "weight", is_visible=States_pagina.campos_visibles["Peso_Estructura"]),
                  crear_select(
                "Acabado",
                "Ingrese el tipo de Acabado",
                "Acabado",
                Acabado,
                States_pagina.valores_campos["Acabado"],
                required=False,
                is_visible=States_pagina.campos_visibles["Acabado"],
                on_change=lambda e: States_pagina.actualizar_campo("Acabado", e)
            ),
            
            # Tratado
            crear_select(
                "Tratado",
                "Ingrese el tipo de tratado",
                "Tratado",
                Tratado,
                States_pagina.valores_campos["Tratado"],
                required=False,
                is_visible=States_pagina.campos_visibles["Tratado"],
                on_change=lambda e: States_pagina.actualizar_campo("Tratado", e)
            ),
             crear_forma("Peso Millar", "Ingrese el Peso", "number", "Peso_Millar", "weight", is_visible=States_pagina.campos_visibles["Peso_Millar"]),
             crear_select(
                "Tipo de Bolsa",
                "Ingrese el tipo de bolsa",
                "Tipo_Bolsa",
                Tipo_Bolsa,
                States_pagina.valores_campos["Tipo_Bolsa"],
                required=False,
                is_visible=States_pagina.campos_visibles["Tipo_Bolsa"],
                on_change=lambda e: States_pagina.actualizar_campo("Tipo_Bolsa", e)
            ),
            crear_select(
                "Tipo de Selle",
                "Ingrese el tipo de selle",
                "Tipo_Selle",
                Tipo_Selle,
                States_pagina.valores_campos["Tipo_Bolsa"],
                required=False,
                is_visible=States_pagina.campos_visibles["Tipo_Bolsa"],
                on_change=lambda e: States_pagina.actualizar_campo("Tipo_Bolsa", e)
            ),
            crear_select(
                "Tipo de Troquel",
                "Ingrese el tipo de troquel",
                "Tipo_Troquel",
                Tipo_Troquel,
                States_pagina.valores_campos["Tipo_Troquel"],
                required=False,
                is_visible=States_pagina.campos_visibles["Tipo_Troquel"],
                on_change=lambda e: States_pagina.actualizar_campo("Tipo_Troquel", e)
            ),
              crear_select(
                "Tipo de Solapa",
                "Ingrese el tipo de Solapa",
                "Tipo_Solapa",
                Tipo_Solapa,
                States_pagina.valores_campos["Tipo_Solapa"],
                required=False,
                is_visible=States_pagina.campos_visibles["Tipo_Solapa"],
                on_change=lambda e: States_pagina.actualizar_campo("Tipo_Solapa", e)
            ),

            crear_forma("Solapa", "Ingrese la solapa", "number", "Solapa", "weight", is_visible=States_pagina.campos_visibles["Solapa"]),
             

                 crear_forma(
                "Fuelle Lateral",
                "Ingrese el Fuelle Lateral",
                "number",
                "Fuelle_Izquierdo",
                "ruler",
                is_visible=States_pagina.campos_visibles["Fuelle_izquierdo"],
                #on_change=lambda e: State_Rollo.actualizar_campo("Fuelle_Izquierdo", e),
                ),
                crear_forma(
                    "Fuelle Frontal",
                    "Ingrese el Fuelle Frontal",
                    "number",
                    "Fuelle_Derecho",
                    "ruler",
                    is_visible=States_pagina.campos_visibles["Fuelle_derecho"],
                    #on_change=lambda e: State_Rollo.actualizar_campo("Fuelle_derecho", e),
                ),
                crear_forma(
                    "Referencia",
                    "Ingrese la Referencia",
                    "Str",
                    "Referencia",
                    "ruler",
                    is_visible=States_pagina.campos_visibles["Referencia"],
                    #on_change=lambda e: State_Rollo.actualizar_campo("Fuelle_derecho", e),
                ),
                 rx.input(
                placeholder="Ingrese el Código Siigo",
                value=States_pagina.Codigo_Siigo,  # Vincular al estado
                on_change=lambda e: States_pagina.actualizar_campo("Codigo_Siigo", e),
                style={
                            "height": "40px",
                            "width": "400px",
                            "padding": "8px",
                            "font-size": "14px",
                            "border-radius": "4px",
                            "border": "1px solid #ccc",
                            "box-shadow": "none",
                            "outline": "none",
                        },
                ),      
                    #Boton de creacion de referencias 
                    rx.hstack(
                        rx.button("Crear Referencias",variant="soft", color_scheme="yellow"),
                        #on_click=lambda: State_Rollo.crear_referencia(States_pagina.producto_nuevo),
                        type="button",
                        
                        
                    ),
                    
                    #crear_forma("Referencia Provispol","", "str","Referencia_Provispol","ruler", default_value=State_Rollo.referencia_str, is_visible=True),
                
           
                                
                    # Botones de acción
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancelar", variant="soft", color_scheme="gray"),
                        ),
                        rx.form.submit(
                            rx.dialog.close(rx.button("Agregar Referencia")),
                            as_child=True,
                            type="submit",
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
        ),
        width="100%",
        direction="column",
        spacing="4",
        max_width="450px",
        padding="1.5em",
        border_radius="25px",
    ) 
    

# Convertir claves y grupos a una lista de diccionarios
# Opciones iniciales para el selector de tipo de producto

items_tipo_producto: list = list(Grupos_por_Tipo_Producto.keys()),
items_grupo = States_pagina.grupos_disponibles  # Sin transformar a diccionarios
      

def rollo_form():
    return rx.form(
        rx.vstack(
            # Título del formulario
            rx.text("Creación de referencia para Rollos", weight="bold", size="3"),
            rx.text(
                "Por favor complete los campos opcionales y seleccione las características del producto",
                italic=True,
                margin_bottom="1em",
            ),
            rx.text("Selecciona los parámetros que desea agregar:", weight="bold"),
            
                    # Selección del Tipo de Producto
                    rx.flex(
            rx.text("Seleccione el Tipo de Producto", font_weight="bold", margin_bottom="0.5em"),
            rx.select(
                Tipo_Producto_Rollos,  # Opciones del tipo de producto
                placeholder="Elija el Tipo de Producto",
                name="Tipo_Producto",
                required=True,
                #on_change= lambda e: States_pagina.producto_nuevo("Tipo_Producto", e),
                on_change=States_pagina.actualizar_tipo_producto,
                #on_change=lambda e:  State_Rollo.actualizar_campo("Tipo_Producto", e),
            ),
            width="100%",
            justify="center",
            flex_wrap="nowrap",
            direction="column",
        ),

        rx.flex(
            rx.text("Seleccione el Grupo", font_weight="bold", margin_bottom="0.5em"),
            rx.select(
                items=items_grupo,
                placeholder="Elija el Grupo",
                name="Grupo",
                required=True,
                on_change=States_pagina.actualizar_grupo,
            ),
            width="100%",
            justify="center",
            flex_wrap="nowrap",
            direction="column",
        ),

        
            
            crear_select(
                "Material 1",
                "Ingrese el Material 1",
                "Material_1",
                Material,
                value=States_pagina.valores_campos["Material_1"],
                required=False,
                is_visible=True,
                on_change=lambda e: States_pagina.actualizar_campo("Material_1", e),

            ),
        

            crear_select(
                "Material 2",
                "Ingrese el Material 2",
                "Material_2",
                Material,
                States_pagina.valores_campos["Material_2"],
                required=False,
                is_visible=States_pagina.campos_visibles["Material_2"],
                on_change=lambda e: States_pagina.actualizar_campo("Material_2", e),
            ),
            crear_select(
                "Material 3",
                "Ingrese el Material 3",
                "Material_3",
                Material,
                States_pagina.valores_campos["Material_3"],
                required=False,
                is_visible=States_pagina.campos_visibles["Material_3"],
                on_change=lambda e: States_pagina.actualizar_campo("Material_3", e),
            ),
            
            # Selección de Color
            crear_select(
                "Color",
                "Ingrese el Color",
                "Color",
                Color,
                value=States_pagina.valores_campos["Color"],
                required=False,
                is_visible=States_pagina.campos_visibles["Color"],
                on_change=lambda e: States_pagina.actualizar_campo("Color", e),
                
                
            ),
            
            # Campos de dimensiones
            rx.flex(
                crear_forma("Ancho", "Ingrese el Ancho", "number", "Ancho", "ruler", is_visible=True,on_change=lambda e:  States_pagina.actualizar_campo("Ancho", e)),
                
                crear_select(
                    "Unidades Ancho",
                    "Ingrese las unidades",
                    "Unidades_Ancho",
                    Unidades_Ancho,
                    States_pagina.valores_campos["Unidades_Ancho"],
                    required=True,
                    on_change=lambda e:  States_pagina.actualizar_campo("Unidades_Ancho", e),
                   
                ),
                width="100%",
                justify="center",
                flex_wrap="nowrap",
                direction="column",
            ),
            
            rx.flex(
                crear_forma("Largo", "Ingrese el Largo", "number", "Largo", "ruler", is_visible=True,on_change=lambda e:  States_pagina.actualizar_campo("Largo", e)),
                crear_select(
                    "Unidades Largo",
                    "Ingrese las unidades",
                    "Unidades_Largo",
                    Unidades_Largo,
                    States_pagina.valores_campos["Unidades_Largo"],
                    required=True,
                    on_change=lambda e:  States_pagina.actualizar_campo("Unidades_Largo", e),
                ),
                width="100%",
                justify="center",
                flex_wrap="nowrap",
                direction="column",
            ),
            
            rx.flex(
                crear_forma("Calibre", "Ingrese el Calibre", "number", "Calibre", "ruler", is_visible=True,on_change=lambda e: States_pagina.actualizar_campo("Calibre", e)),
                crear_select(
                    "Unidades Calibre",
                    "Ingrese las unidades",
                    "Unidades_Calibre",
                    Unidades_Calibre,
                    States_pagina.valores_campos["Unidades_Calibre"],
                    required=True,
                    on_change=lambda e: States_pagina.actualizar_campo("Unidades_Calibre", e),
                   
                ),
                width="100%",
                justify="center",
                flex_wrap="nowrap",
                direction="column",
            ),
            
            # Peso por Estructura
            crear_forma("Peso por Estructura", "Ingrese el Peso", "number", "Peso_Estructura", "weight", is_visible=States_pagina.campos_visibles["Peso_Estructura"]),
            
            # Tipo y Número de Bobinado
            crear_select(
                "Tipo de Bobinado",
                "Tipo de Bobinado",
                "Tipo_Bobinado",
                Tipo_Bobinado,
                States_pagina.valores_campos["Tipo_Bobinado"],
                required=True,
                #is_visible=States_pagina.campos_visibles["Tipo_Bobinado"],
                on_change=lambda e: States_pagina.actualizar_campo("Tipo_Bobinado", e),
            ),
            crear_select(
                "Número de Bobinado",
                "Ingrese el número de bobinado",
                "Numero_Bobinado",
                Numero_Bobinado,
                States_pagina.valores_campos["Numero_Bobinado"],
                required=True,
                is_visible=States_pagina.campos_visibles["Numero_Bobinado"],
            ),
            
            # Peso Rollo
            crear_forma("Peso Rollo", "Ingrese el peso por Rollo", "str", "Peso Rollo", "ruler", is_visible=True),
            
            # Fuelle Izquierdo y Derecho
            crear_forma(
                "Fuelle Izquierdo",
                "Ingrese el Fuelle Izquierdo",
                "number",
                "Fuelle_Izquierdo",
                "ruler",
                is_visible=States_pagina.campos_visibles["Fuelle_izquierdo"],
                on_change=lambda e: States_pagina.actualizar_campo("Fuelle_Izquierdo", e),
            ),
            crear_forma(
                "Fuelle Derecho",
                "Ingrese el Fuelle Derecho",
                "number",
                "Fuelle_Derecho",
                "ruler",
                is_visible=States_pagina.campos_visibles["Fuelle_derecho"],
                on_change=lambda e: States_pagina.actualizar_campo("Fuelle_Derecho", e),
            ),
            
            # Acabado
            crear_select(
                "Acabado",
                "Ingrese el tipo de Acabado",
                "Acabado",
                Acabado,
                States_pagina.valores_campos["Acabado"],
                required=False,
                is_visible=States_pagina.campos_visibles["Acabado"],
                on_change=lambda e: States_pagina.actualizar_campo("Acabado", e)
            ),
            
            # Tratado
            crear_select(
                "Tratado",
                "Ingrese el tipo de tratado",
                "Tratado",
                Tratado,
                States_pagina.valores_campos["Tratado"],
                required=False,
                is_visible=States_pagina.campos_visibles["Tratado"],
                on_change=lambda e: States_pagina.actualizar_campo("Tratado", e)
            ),
            
         
            crear_forma("Referencia", "Ingrese la Referencia", "str", "Referencia", "ruler", is_visible=True, on_change=lambda e: States_pagina.actualizar_campo("Referencia", e)),
           
            rx.input(
                placeholder="Ingrese el Código Siigo",
                value=States_pagina.Codigo_Siigo,  # Vincular al estado
                on_change=lambda e: States_pagina.actualizar_campo("Codigo_Siigo", e),
                style={
                            "height": "40px",
                            "width": "400px",
                            "padding": "8px",
                            "font-size": "14px",
                            "border-radius": "4px",
                            "border": "1px solid #ccc",
                            "box-shadow": "none",
                            "outline": "none",
                        },
                ),    

            rx.hstack(
                rx.button("Crear Referencias",variant="soft", color_scheme="yellow"),
                on_click=lambda: States_pagina.actualizar_form_data(),
                type="button",
                
                
            ),
            
            #crear_forma("Referencia Provispol","", "str","Referencia_Provispol","ruler", default_value=State_Rollo.referencia_str, is_visible=True),
           
                rx.flex(
                    rx.input(
                        placeholder="Referencia Provispol",
                        value=States_pagina.referencia_str,  # Vincular al estado
                        is_visible=True,
                        #on_change= lambda e : States_pagina.actualizar_campo("Referencia_Provispol", e),
                        style={
                            "height": "40px",
                            "width": "400px",
                            "padding": "8px",
                            "font-size": "14px",
                            "border-radius": "4px",
                            "border": "1px solid #ccc",
                            "box-shadow": "none",
                            "outline": "none",
                        },
                    ),
                    rx.button(
                        "Copiar",
                        on_click=States_pagina.copiar_referencia,  # Evento personalizado
                        variant="soft",
                        color_scheme="green",
                        height="40px",
                    ),
                    padding_top="1em",
                    spacing="1",
                    mt="4",
                    justify="center",
                
                ),
                    

                        
            # Botones de acción
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", variant="soft", color_scheme="gray"),
                    on_click=States_pagina.limpiar_datos_producto
                ),
                rx.form.submit(
                    rx.dialog.close(rx.button("Agregar Referencia")),
                    as_child=True,
                    type="submit",
                    on_click = lambda: States_pagina.agregarProducto_to_db(States_pagina.producto_nuevo),
                    reset_on_submit=True,
                     
                ),
                padding_top="2em",
                spacing="3",
                mt="4",
                justify="end",
            ),
        ),
        #on_submit=State_Rollo.actualizar_form_data,
        #on_submit=States_pagina.agregarProducto_to_db,
        
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
         rx.text("Creacion de referencia para Rollos Proviagro", weight="bold", size="2"),
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
         rx.text("Creacion de referencia para Servicios", weight="bold", size="2"),
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

    
    

        
    
    