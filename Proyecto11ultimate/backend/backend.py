import reflex as rx
# from typing import Union
from sqlmodel import Session,select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta
from ..backend.productos_model import Rollo
from ..backend.connect_db import connect
from ..backend.metodosdb import select_rollo
from ..views.Listados import Grupos_por_Tipo_Producto, valor_exepcional, Campos_por_Tipo, Valores_predeterminados
from ..components.CrearReferencias import State_Rollo
#el metodo looad entries se llama cuando el usuario interaqctua con los filtros y valores 
#que tenemos entonces con cualquiera de esas inteccaciones se llama a ese metodo 
#Pero antes de eso vamos a ingresar el metodo de enviar un producto a la base de datos, 
#luego de crear ese metodo lo que seguiria seria pues asignarle el estado al boton de crear
#luego de que eso funcione ya solo lo que deberiamos hacer es la funcion de load entrys que 
#me ayudara a mostrar los productos creados y filtrarlos eso por ahora ya veremos que ma hay por hacer

class States_pagina(rx.State):
    # rollo: list[Rollo] = []  # Inicializamos la lista vacía para evitar errores
    rollos: list[Rollo] =[]
    producto_nuevo: dict = {}
    selected_product: str = "Bolsa"  # Producto seleccionado en la interfaz.
    buscar_valor: str = ""
    nombre_columna: str = "" # este es lomismo que sort_value
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
                    query = query.where(
                        or_(
                            [
                                getattr(Rollo, field).ilike(buscar_valor)
                                for field in fields
                                if field not in [
                                    "Ancho", "Calibre", "Largo", "PesoPorRollo",
                                    "UnidadesCalibre", "UnidadesLargo", "unidadesAncho", "Codigo_Siigo"
                                ]
                            ]
                            + [cast(Rollo.Codigo_Siigo, String).ilike(buscar_valor)]
                        )
                    )
                except Exception as e:
                    print(f"Error al construir el filtro de búsqueda: {e}")
            
            # Ordenar los resultados
            if self.nombre_columna:
                print(f"Columna para ordenar: {self.nombre_columna}")
                try:
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
        State_Rollo.actualizar_campo = ( "Tipo_Producto", tipo)
            
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
        self.grupo_seleccionado = grupo  # Actualizamos el grupo seleccionado

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

    #@rx.event    
    def agregarProducto_to_db(self, form_data: dict):
        # Asignamos los datos del formulario al producto nuevo
        self.producto_nuevo = form_data
        # Agregamos la fecha actual a los datos
        self.producto_nuevo["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # # Validamos que los campos requeridos no sean None o vacíos
        # if not self.producto_nuevo.get('Material_1'):
        # self.producto_nuevo['Material_1'] = 'PEBD'  # Asignar un valor predeterminado
    
        # Aquí puedes agregar más validaciones de campos según sea necesario

        try:
            with rx.session() as session:
                # Verificamos si ya existe un producto con el mismo código Siigo
                if session.exec(
                    select(Rollo).where(Rollo.Codigo_Siigo == self.producto_nuevo["Codigo_Siigo"])
                ).first():
                    return rx.window_alert("La referencia con este código Siigo ya está registrada")
                
                # Imprimimos los datos para depuración
                print("Producto nuevo:", self.producto_nuevo)
                
                # Asignamos los datos al modelo Rollo
                producto_nuevo = Rollo(**self.producto_nuevo)

                # Verificamos que el objeto Rollo esté correctamente asignado
                print("Producto nuevo asignado:", producto_nuevo)

                # Agregamos el producto a la base de datos
                session.add(producto_nuevo)
                session.commit()
                self.cargar_productos()
            
            # Notificamos que el producto fue agregado exitosamente
            return rx.toast.info(f"Referencia con código SIIGO {self.producto_nuevo['Codigo_Siigo']} ha sido agregada.", position="bottom-right")
        
        except Exception as e:
            # Mostramos el error en la consola y en la alerta
            print(f"Error al agregar el producto: {str(e)}")
            print("Datos del producto:", self.producto_nuevo)  # Mostramos los datos para depurar
            return rx.window_alert(f"Error al agregar el producto: {str(e)}")
              
        #toast es una notificación en la UI}
     #metodos que llama al metodo de cargar_productos


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
           
    def nombre_columnas(self, nombre_columna: str):
        self.nombre_columna = nombre_columna
        self.cargar_productos()

    def alternar_orden(self):
        self.order_table = not self.order_table
        self.cargar_productos()

    def filtrar_valores(self, buscar_valor):
        self.buscar_valor = buscar_valor
        self.cargar_productos()    
    def get_productos(self, rollo:Rollo):
        self.producto_nuevo = rollo   