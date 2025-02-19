import reflex as rx
import re
# from typing import Union
from sqlmodel import Session,select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta
from ..backend.productos_model import Rollo
from ..backend.connect_db import connect
from ..backend.metodosdb import select_rollo
from ..views.Listados import Grupos_por_Tipo_Producto, valor_exepcional, Campos_por_Tipo, Valores_predeterminados
from ..components.CrearReferencias import ORDEN_CAMPOS_ROLLOS, CAMPOS, LITERALES_FIJOS, Grupos_Especiales
#el metodo looad entries se llama cuando el usuario interaqctua con los filtros y valores 
#que tenemos entonces con cualquiera de esas inteccaciones se llama a ese metodo 
#Pero antes de eso vamos a ingresar el metodo de enviar un producto a la base de datos, 
#luego de crear ese metodo lo que seguiria seria pues asignarle el estado al boton de crear
#luego de que eso funcione ya solo lo que deberiamos hacer es la funcion de load entrys que 
#me ayudara a mostrar los productos creados y filtrarlos eso por ahora ya veremos que ma hay por hacer

class States_pagina(rx.State):
    # rollo: list[Rollo] = []  # Inicializamos la lista vacía para evitar errores
    rollos: list[Rollo] =[]
    referencia_str: str = ""
    producto_nuevo: dict = {}
    form_data: dict = {}
    Codigo_Siigo: str = ""
    selected_product: int = 0  # Producto seleccionado en la interfaz.
    buscar_valor: str = ""
    nombre_columna: str = "Codigo_Siigo" # este es lomismo que sort_value
    order_table: bool = False # este es el mismo sort_reverse
    tipo_producto: str = ""  # Tipo de producto seleccionado
    grupos_disponibles: list[str] = []  # Lista de grupos disponibles según el tipo de producto
    grupo_seleccionado: str = ""  # Grupo seleccionado por el usuario
    campos_visibles: dict[str, bool] = {}  # Estado de visibilidad de los campos
    valores_campos: dict[str, str] = {}
    rollos_eliminados: list[Rollo] = [] 
    

    #creacion de funcion que carga todos los productos en la tabla 
    
    @rx.event
    def cargar_productos(self) -> list[Rollo]:
        print("Se llamó a la función cargar_productos")

        with rx.session() as session:
            query = select(Rollo).where(Rollo.estado_eliminado == False)  # Filtrar no eliminados

            # Filtro de búsqueda
            if self.buscar_valor:
                buscar_valor = f"%{str(self.buscar_valor).lower()}%"
                print(f"Valor de buscar_valor: {self.buscar_valor}")

                try:
                    fields = Rollo.get_fields()
                    print(f"Campos retornados por Rollo.get_fields(): {fields}")
                    text_fields = ["Codigo_Siigo", "Material", "fecha", "Grupo"]
                    conditions = []

                    for field in fields:
                        if field not in [
                            "Ancho", "Calibre", "Largo", "PesoPorRollo",
                            "UnidadesCalibre", "UnidadesLargo", "unidadesAncho", "Codigo_Siigo"
                        ]:
                            conditions.append(getattr(Rollo, field).ilike(buscar_valor))

                    # Agregar filtro específico para `Codigo_Siigo`
                    conditions.append(cast(Rollo.Codigo_Siigo, String).ilike(buscar_valor))

                    # Combinar todas las condiciones con `or_`
                    query = query.where(or_(*conditions))
                except Exception as e:
                    print(f"Error al construir el filtro de búsqueda: {e}")

            # Ordenar los resultados
            if self.nombre_columna:
                print(f"Columna para ordenar: {self.nombre_columna}")
                try:
                    if not hasattr(Rollo, self.nombre_columna):
                        raise AttributeError(f"La columna '{self.nombre_columna}' no es válida.")

                    sort_column = getattr(Rollo, self.nombre_columna)
                    print(f"Columna válida para ordenar: {sort_column}")

                    if self.nombre_columna == "Codigo_Siigo":
                        order = desc(sort_column) if self.order_table else asc(sort_column)
                    else:
                        order = desc(func.lower(sort_column)) if self.order_table else asc(func.lower(sort_column))

                    query = query.order_by(order)
                except AttributeError as e:
                    print(f"Error en la ordenación, columna no válida: {e}")
                except Exception as e:
                    print(f"Otro error al construir la ordenación: {e}")

            # Ejecutar la consulta
            try:
                self.rollos = session.exec(query).all()
                print(f"Productos cargados: {len(self.rollos)} encontrados.")
            except Exception as e:
                print(f"Error al ejecutar la consulta: {e}")
          
        
        
    @rx.event
    def cargar_productos_eliminados(self) -> list[Rollo]:
        print("Se llamó a la función cargar_productos_eliminados")

        with rx.session() as session:
            query = select(Rollo).where(Rollo.estado_eliminado == True)  # Filtrar eliminados

            # Ejecutar la consulta
            try:
                self.rollos = session.exec(query).all()
                print(f"Productos eliminados cargados: {len(self.rollos)} encontrados.")
            except Exception as e:
                print(f"Error al ejecutar la consulta de productos eliminados: {e}")
        
        
    
    def actualizar_tipo_producto(self, tipo: str):
        """
        Actualiza el tipo seleccionado y obtiene los grupos disponibles para ese tipo.
        """
        #State_Rollo.actualizar_campo = ( "Tipo_Producto", tipo)
        self.actualizar_campo("Tipo_Producto", tipo)    
        self.tipo_producto = tipo
        

        # print(f"Campo 'Tipo_Producto' actualizado con el valor: {tipo}")


        self.grupo_seleccionado = ""  # Reinicia el grupo seleccionado

        if tipo in Campos_por_Tipo:
            # Obtiene los grupos disponibles para el tipo
            self.grupos_disponibles = list(Campos_por_Tipo[tipo].keys())
        else:
            # Si el tipo no existe, limpia los datos
            self.grupos_disponibles = []
            self.campos_visibles = {}
        
        
        print(f"Tipo seleccionado: {tipo}")
        print(f"Grupos disponibles: {self.grupos_disponibles}")
        print(f"Campos predeterminados: {self.valores_campos}")
        #return self.call_handler("State_Rollo.actualizar_campo", "Tipo_Producto", tipo)
    def actualizar_grupo(self, grupo: str):
        """
        Actualiza el grupo seleccionado, obtiene las claves de los campos visibles
        y asigna los valores predeterminados si existen para ese grupo.
        """

        self.actualizar_campo("Grupo", grupo)  # Actualizamos el grupo
        self.grupo_seleccionado = grupo  # Actualizamos el grupo seleccionado
        self.generar_prefijo_codigo_siigo(grupo)  # Generar prefijo del Código Siigo    

        # Verificar si el grupo existe en Campos_por_Tipo
        if (
            self.tipo_producto in Campos_por_Tipo
            and grupo in Campos_por_Tipo[self.tipo_producto]
        ):
            # Obtiene los campos visibles
            self.campos_visibles = Campos_por_Tipo[self.tipo_producto][grupo]
        else:
            self.campos_visibles = valor_exepcional

        # Verificar si el grupo tiene valores predeterminados
        if grupo in Valores_predeterminados:
            self.valores_campos = Valores_predeterminados[grupo]

            # Lógica adicional: actualiza cada campo predeterminado
            for campo, valor in self.valores_campos.items():
                self.actualizar_campo(campo, valor)  # Llamada explícita a actualizar_campo

        else:
            self.valores_campos = {}  # Reseteamos si no hay valores predeterminados

        # Depuración
        print(f"Grupo seleccionado: {grupo}")
        print(f"Campos visibles: {self.campos_visibles}")
        print(f"Campos predeterminados: {self.valores_campos}")

   
    def update_selected(self, selected_product):
        self.selected_product = selected_product

    def get_all_products(self):
          print("Ejecutando get_all_products")  # Confirmación de que la función se llama
          resultado = select_rollo()
          print("Resultado de select_rollo:", resultado)  # Imprimir el resultado para depuración
          self.rollos = resultado  # Asigna el resultado a la variable de estado

    def actualizar_campo(self, campo: str, valor: str):
        """
        Actualiza un campo específico en el diccionario form_data.
        """
        # Asegúrate de actualizar el diccionario correctamente
        self.producto_nuevo[campo] = valor
        
        print(f"Campo actualizado: {campo} -> {valor}")
        print(f"Datos del producto actualizados: {self.producto_nuevo}")
    def determinar_literal(self, campo, form_data):
      
        if campo == "R-":
            grupo = form_data.get("Tipo_Producto", "").strip()
            if grupo == "Plástico para invernadero": 
                return "R*-"
            return "R-"
        
    # Puedes agregar más reglas aquí para otros literales dinámicos
        return LITERALES_FIJOS.get(campo, "")
    
    def actualizar_form_data(self):
       
        def generar_referencia(form_data, orden_campos):
                referencia_ordenada = []
                grupo = form_data.get("Grupo", "").strip()
                if grupo in Grupos_Especiales:
                    literal_especial = Grupos_Especiales[grupo]
                    form_data["Literal_Especial"] = literal_especial  # Actualizar el valor del campo
                    orden_campos["Literal_Especial"] = True  # Activar el campo para incluirlo en la referencia

                tipo_producto = form_data.get("Tipo_Producto", "").strip()
                if tipo_producto == "Plástico para invernadero":  # Reemplaza con la condición específica
                    # Mover Tipo_Bobinado al final
                    orden_campos = {k: v for k, v in orden_campos.items() if k != "Tipo_Bobinado"}  # Eliminar de la posición actual
                    orden_campos["ESPACIO_7"] = True  # Asegurarse de que el espacio 7 esté antes del final
                    orden_campos["Tipo_Bobinado"] = True  # Agregar Tipo_Bobinado al final

                    # Reemplazar Material_1 con el valor del grupo seleccionado
                    form_data["Material_1"] = grupo
                    # Si el campo es un espacio, agregarlo directamente
                for campo, incluir in orden_campos.items():
                    if "Unidades_" in campo:
                        campo_principal = campo.replace("Unidades_", "")
                        if not form_data.get(campo_principal):  # Si el campo principal no tiene valor
                            continue  # Saltar este campo de unidades
    # Detectar claves especiales de espacio
                    if "ESPACIO" in campo and incluir:
                        referencia_ordenada.append(" ")  # Agregar un espacio explícito
                        continue

                    # Literales dinámicos o fijos
                    if campo == "R-":
                        if incluir:
                            literal = self.determinar_literal(campo, form_data)
                            if literal:
                                referencia_ordenada.append(f"{literal}")  # Espacio antes y después del literal
                            orden_campos[campo] = True
                        continue

                    # Si el campo está en form_data
                    if campo in form_data:
                        valor = form_data.get(campo, "").strip()
                        valor_traducido = CAMPOS.get(campo, {}).get(valor, valor)  # Traducir valor si aplica
                 
                        if campo == "Referencia":
                            if valor_traducido:  # Verificar si el valor no está vacío o nulo
                                referencia_ordenada.append(f"Ref {valor_traducido}")
                                orden_campos[campo] = True
                            continue
                        # Si el campo tiene un literal fijo, agregarlo
                       # Si el campo tiene un literal fijo, agregarlo
                        if campo in LITERALES_FIJOS:
                            if valor_traducido:  # Solo si hay un valor válido
                                literal = LITERALES_FIJOS[campo]
                                
                                # Si el campo es un fuelle, invertir el orden (poner el literal antes)
                                if campo in ["Fuelle_Izquierdo", "Fuelle_Derecho"]:
                                    referencia_ordenada.append(f"{literal}{valor_traducido}")
                                else:
                                    referencia_ordenada.append(f"{valor_traducido}{literal}")  # Orden normal
                                
                                orden_campos[campo] = True  # Actualizar estado del campo
                            continue

                            
                        # Solo incluir valores válidos
                        if valor_traducido:
                            referencia_ordenada.append(f"{valor_traducido}")  # Agregar valor traducido
                            orden_campos[campo] = True  # Actualizar estado del campo

                # Unir la referencia ordenada en una sola cadena
                referencia = "".join(referencia_ordenada).strip()

                return referencia

        print("Datos del formulario actualizados:", self.producto_nuevo)

        # Crear una copia de ORDEN_CAMPOS_ROLLOS para modificar su estado
        orden_campos_actualizado = ORDEN_CAMPOS_ROLLOS.copy()
        self.form_data = self.producto_nuevo.copy()

        # Generar la referencia usando la lógica dinámica
        self.referencia_str = generar_referencia(self.form_data, orden_campos_actualizado)

        print("Referencia generada:", self.referencia_str)
        print("Estado de los campos:", orden_campos_actualizado)

    def limpiar_datos_producto(self):
        """
        Limpia los datos de producto_nuevo y otras variables relacionadas.
        """
        self.producto_nuevo = {}
        self.form_data.clear()
        self.referencia_str = ""
        self.Codigo_Siigo = ""
        print("Datos del producto y formulario limpiados.")   
    
    def agregarProducto_to_db(self, form_data: dict):
        """
        Agrega un producto a la base de datos y limpia los datos si la operación es exitosa.
        """
        self.producto_nuevo["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.producto_nuevo["Referencia_Provispol"] = self.referencia_str
       
        if not self.producto_nuevo.get("Codigo_Siigo"):
            return rx.window_alert("El Código Siigo es obligatorio.")

        try:
            with rx.session() as session:
                # Verificar si el producto ya existe
                if session.exec(
                     select(Rollo)
                    .where(Rollo.Codigo_Siigo == self.Codigo_Siigo)
                    .where(Rollo.estado_eliminado == False)
                ).first():
                    return rx.window_alert(f"La referencia con este código Siigo ({self.producto_nuevo['Codigo_Siigo']}) ya está registrada.")

                # Agregar el producto a la base de datos
                producto_nuevo = Rollo(**self.producto_nuevo)
                session.add(producto_nuevo)
                session.commit()

                # Cargar productos después de la inserción
                self.cargar_productos()

                # Notificar éxito y limpiar datos
                rx.toast.info(
                    f"Referencia con código SIIGO {self.producto_nuevo['Codigo_Siigo']} ha sido agregada.",
                    position="bottom-right",
                )

                # Limpia los datos solo si la operación fue exitosa
                self.limpiar_datos_producto()
                print("Datos del producto y formulario limpiados tras agregar producto exitosamente.")

                #return True  # Devuelve un indicador de éxito

        except Exception as e:
            # Manejo de errores
            print(f"Error al agregar el producto: {str(e)}")
            print("Datos del producto:", self.producto_nuevo)
            return rx.window_alert(f"Error al agregar el producto: {str(e)}")
        
    def generar_prefijo_codigo_siigo(self, grupo: str):
        """
        Genera un prefijo del Código Siigo basado en el grupo seleccionado y actualiza el formulario.
        """
        # Diccionario de regex para grupos
        regex = re.compile(r"(\d{4})")
        match = regex.search(grupo)
        
        if not match:
            raise ValueError(f"El grupo '{grupo}' no tiene un formato válido para extraer el código.")
        
        # Extraer el código y generar el prefijo
        codigo_grupo = match.group(1)
        prefijo = f"2-{codigo_grupo}-"
        
        # Actualizar el formulario directamente
        self.Codigo_Siigo = prefijo
        
        return prefijo
        


    def eliminar_producto(self, Codigo_Siigo: int):
        with rx.session() as session:
            rollo = session.exec(select(Rollo).where(Rollo.Codigo_Siigo == Codigo_Siigo)).first()
            if rollo:
                rollo.estado_eliminado = True  # Cambia el estado a eliminado
                session.commit()
                self.cargar_productos()  # Recarga los productos visibles
                return rx.toast.info(
                    f"Referencia con código Siigo {rollo.Codigo_Siigo} ha sido marcada como eliminada.",
                    position="bottom-right",
                )
            else:
                return rx.toast.error(
                    f"No se encontró el registro con código Siigo {Codigo_Siigo}.",
                    position="bottom-right",
        )
           
    def nombres_columnas(self, nombre_columna: str):
        self.nombre_columna = nombre_columna
        self.cargar_productos()

    @rx.event
    def alternar_orden(self):
        print(f"Orden antes de alternar: {self.order_table}")
        self.order_table = not self.order_table
        print(f"Orden después de alternar: {self.order_table}")
        self.cargar_productos()

    def filtrar_valores(self, buscar_valor):
        self.buscar_valor = buscar_valor
        self.cargar_productos()    
    def get_productos(self, rollo:Rollo):
        self.producto_nuevo = rollo   

    def copiar_referencia(self):
        # Usamos el comando de JavaScript para copiar al portapapeles
        return rx.set_clipboard(self.referencia_str)