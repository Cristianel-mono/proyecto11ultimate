import reflex as rx 
from typing import Dict


#aca es donde nacen las referencias les daremos sus respectivos oredenes y valores
#Crearemos una clase de estado para almacenar todos los valores y crear la referencia.

class State_Rollo(rx.State):
     
    form_data: dict[str, str] = {}
    referencia_str: str = " "
   
#nada que logramos actualizar el campo de tipo 
    
  
    def actualizar_campo(self, campo: str, valor: str):
        """
        Actualiza un campo específico en el diccionario form_data.
        """
        
        self.form_data[campo] = valor
        print(f"Campo actualizado: {campo} -> {valor}")
    
    def actualizar_form_data(self):
        """
        Procesa los datos almacenados en form_data y genera la referencia de manera dinámica.
        """

        def generar_referencia(form_data, orden_campos):
            """
            Genera una referencia dinámica basada en los datos del formulario y el orden de los campos.

            Args:
                form_data (dict): Datos del formulario.
                orden_campos (dict): Diccionario que define el orden y el estado de los campos/literales.

            Returns:
                str: Referencia generada.
            """
            referencia_ordenada = []

            for campo, incluir in orden_campos.items():
                # Si el campo es un literal fijo, depende de su valor en el diccionario
                if not campo.isalpha() and incluir:
                    referencia_ordenada.append(campo)
                    continue

                # Si el campo está en form_data
                if campo in form_data:
                    valor = form_data.get(campo, "").strip()
                    valor = CAMPOS.get(campo, {}).get(valor, valor)  # Traducir valor si aplica

                    # Validar dependencias entre unidades y valores
                    if "Unidades_" in campo:
                        campo_principal = campo.replace("Unidades_", "")
                        if not form_data.get(campo_principal):
                            continue  # Saltar si el campo principal no está presente

                    if valor:  # Solo incluir si hay un valor válido
                        referencia_ordenada.append(valor)
                        orden_campos[campo] = True  # Actualizar estado a True

                 


            return " ".join(referencia_ordenada).strip()

        print("Datos del formulario actualizados:", self.form_data)

        # Crear una copia de ORDEN_CAMPOS_ROLLOS para modificar su estado
        orden_campos_actualizado = ORDEN_CAMPOS_ROLLOS.copy()

        # Generar la referencia usando la lógica dinámica
        self.referencia_str = generar_referencia(self.form_data, orden_campos_actualizado)

        print("Referencia generada:", self.referencia_str)
        print("Estado de los campos:", orden_campos_actualizado)

        # Limpiar los datos del formulario después de generar la referencia
        self.form_data.clear()
        print("Datos del formulario limpiados:", self.form_data)




MATERIAL = {
        "Aluminio": "ALUM",
        "Poliamida Bi-Orientada": "BOPA",
        "Polipropileno Bi-Orientado Mate": "BOPP_Mate",
        "Polipropileno Bi-Orientado Metalizado": "BOPP_Metal",
        "Polipropileno Bi-Orientado Perlado": "BOPP_Perl",
        "Polipropileno Bi-Orientado Transparente": "BOPP_Transp",
        "Polipropileno Cast": "CAST_PP",
        "EVOH Co-extruido": "EVOH_Coext",
        "Polipropileno Mono-Orientado": "MOPP",
        "Nylon Co-extruido": "NYLON_Coext",
        "Papel": "PAPEL",
        "Polietileno de Alta Densidad": "PEAD",
        "Polietileno de Alta Densidad Co-extruído": "PEAD_Coext",
        "Polietileno de Alta Densidad Corriente": "PEAD_Cte",
        "Polietileno de Baja Densidad": "PEBD",
        "Polietileno de Baja Densidad Co-extruido": "PEBD_Coext",
        "Polietileno de Baja Densidad Corriente": "PEBD_Cte",
        "Polietileno de Media Densidad": "PEMD",
        "Polietileno de Media Densidad Co-extruído": "PEMD_Coext",
        "Poliéster Mate": "PET_Mate",
        "Poliéster Metalizado": "PET_Metal",
        "Poliéster Transparente": "PET_Transp",
        "Polipropileno Co-extruído": "PP_Coext",
        "Polietileno Stretch": "Stretch",
}

# Diccionario principal con referencia reutilizable
CAMPOS = {
    "Material_1": MATERIAL,
    "Material_2": MATERIAL,  
    "Material_3": MATERIAL,  
    "Color": {
        "Amarillo": "AMAR",
        "Rojo": "ROJ",
        "Azul": "AZUL",
        "Blanco-Negro": "B/N",
        "Blanco": "BLCO",
        "Naranja": "NARAN",
        "Negro": "NGR",
        "Transparente": "TRANSP",
        "Verde": "VERDE",
        "Blanco-Blanco": "BLCO/BLCO",
        "Gris": "GRIS",
        "Plata-Negro": "PLATA/NGR",
    },
    "Unidades_Ancho": {
        "Centímetros(cm)": "cm *",
        "Milímetros(mm)": "mm *",
        "Pulgadas(in)": "in *",
    },
    "Unidades_Largo": {
        "Centímetros(cm)": "cm",
        "Milímetros(mm)": "mm",
        "Pulgadas(in)": "in",
        "Metros(m)": "m",
    },
    "Unidades_Calibre": {
        "Milésimas de pulgada(mils)": "mils *",
        "Micras(mic)": "mic *",
    },
    "Tipo_Bobinado": {
        "Tubular": "TUB",
        "Semitubular": "STUB",
        "Lámina": "LAM",
        "Lámina doble": "LAM_DOB",
    },
    "Acabado": {
        "Grafilado": "GRAF",
        "Liso": "LISO",
        "Macro Perforado": "MAC_Perf",
        "Micro Perforado": "MIC_Perf",
    },
    "Tratado": {
        "SIN TRATAR": "ST",
        "TRATADO 1 CARA": "T1C",
        "TRATADO 2 CARA": "T2C",
    },
}

ORDEN_CAMPOS_ROLLOS = { 
    "Tipo_Producto": False,  
    "R-":True,
    "Material_1":False,
    " ":True,
    "Color":False,          
    " " :True,
    "Ancho":False,          
    "Unidades_Ancho":False, 
    "*":False, # Literal fijo ancho             
    "Calibre":False,        
    "Unidades_Calibre":False, 
    "*":False,  # Literal fijo calibre         
    "Largo":False,          
    "Unidades_Largo":False, 
    "Tipo_Bobinado":False,  
    "Ref":False,           
    "referencia":False,     
  }
