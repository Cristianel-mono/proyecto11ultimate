#Listados de producto Rollo
Grupo: list = [
    "ROLLO PEBD ORIGINAL", 
    "ROLLO PEBD CORRIENTE", 
    "ROLLO PEBD SEMIORIGINAL", 
    "ROLLO PEBD COEXTRUIDO", 
    "ROLLO PEAD ORIGINAL", 
    "ROLLO PEBD TERMOENCOGIBLE", 
    "ROLLO MOPP", 
    "ROLLO BOPP", 
    "ROLLO CATPP", 
    "ROLLO STRETCH", 
    "ROLLO PROVIAGRO ENERGY", 
    "ROLLO PROVIAGRO LUMINANCE", 
    "ROLLO PROVIAGRO SPECTRUM", 
    "ROLLO PROVIAGRO BLACK", 
    "ROLLO PEBD ANCHO", 
    "ROLLO PEBD CORRIENTE ANCHO", 
    "ROLLO NEGRO SEMIORIGINAL"
]
Material: list[str] = [
    "Aluminio",
    "Poliamida Bi-Orientada",
    "Polipropileno Bi-Orientado Mate",
    "Polipropileno Bi-Orientado Metalizado",
    "Polipropileno Bi-Orientado Perlado",
    "Polipropileno Bi-Orientado Transparente",
    "Polipropileno Cast",
    "EVOH Co-extruido",
    "Polipropileno Mono-Orientado",
    "Nylon Co-extruido",
    "Papel",
    "Polietileno de Alta Densidad",
    "Polietileno de Alta Densidad Co-extruído",
    "Polietileno de Alta Densidad Corriente",
    "Polietileno de Baja Densidad",
    "Polietileno de Baja Densidad Co-extruido",
    "Polietileno de Baja Densidad Corriente",
    "Polietileno de Media Densidad",
    "Polietileno de Media Densidad Co-extruído",
    "Poliéster Mate",
    "Poliéster Metalizado",
    "Poliéster Transparente",
    "Polipropileno Co-extruído",
    "Polietileno Stretch",
]


Color: list = [
    "Amarillo", 
    "Azul", 
    "Blanco-Negro", 
    "Blanco", 
    "Naranja", 
    "Negro", 
    "Rojo",
    "Transparente", 
    "Verde", 
    "Blanco-Blanco", 
    "Gris", 
    "Plata-Negro"
]

Tipo_Producto: list = [
    "Rollo sin impresión", 
    "Rollo con impresión", 
    "Rollo bilaminado sin impresión", 
    "Rollo bilaminado con impresión", 
    "Rollo trilaminado sin impresión", 
    "Rollo trilaminado con impresión",
    "Rollo refilado sin impresión", 
    "Rollo refilado con impresión", 
    "Plástico para invernadero",
    "Rollo acolchado/mulch", 
    "Rollo negro aditivado",
]
#preguntar si estan bien las unidades de esta manera 
Unidades_Ancho: list[str] = [
"cm",
"mm",
"in",

]
Unidades_Largo: list = [
"cm",
"mm",
"in",
"m",
  
]
Undiades_Calibre: list = [
 "mils",
 "mic",  
]
Grupos_por_Tipo_Producto =  {
    "Rollo sin impresión": [
        "ROLLO PEBD ORIGINAL-SIN IMPRESION-1101",
        "ROLLO PEBD CORRIENTE-SIN IMPRESION-1102",
        "ROLLO PEBD SEMIORIGINAL-SIN IMPRESION-1103",
        "ROLLO PEBD COEXTRUIDO-SIN IMPRESION-1104",
        "ROLLO PEAD ORIGINAL-SIN IMPRESION-1105",
        "ROLLO PEAD CORRIENTE-SIN IMPRESION-1106",
        "ROLLO PEBD TERMOENCOGIBLE-SIN IMPRESION-1107",
        "ROLLO MOPP-SIN IMPRESION-1108",
        "ROLLO BOPP-SIN IMPRESION-1109",
        "ROLLO CASTPP-SIN IMPRESION-1111",
        "ROLLO STRETCH-SIN IMPRESION-1112",
        "ROLLO NEGRO SEMIORIGINAL-SIN IMPRESION-1122",
        "ROLLO PEBD ANCHO-SIN IMPRESION-1120",
        "ROLLO PEBD CORRIENTE ANCHO-SIN IMPRESION-1121",
        "ROLLO SIN FIN PEBD ORIGINAL-SIN IMPRESION-1401",
        "ROLLO CENEFA PEBD ORIGINAL-SIN IMPRESION-1501",
    ],
    "Rollo con impresión": [
        "ROLLO PEBD ORIGINAL-1101",
        "ROLLO PEBD CORRIENTE-1102",
        "ROLLO PEBD SEMIORIGINAL-1103",
        "ROLLO PEBD COEXTRUIDO-1104",
        "ROLLO PEAD ORIGINAL-1105",
        "ROLLO PEAD CORRIENTE-1106",
        "ROLLO MOPP-1108",
        "ROLLO BOPP-1109",
        "ROLLO CASTPP-1111",
        "ROLLO NEGRO SEMIORIGINAL-1122",
    ],
    "Rollo bilaminado sin impresión": [
        "ROLLO LAMINADO-1600-BI-SIN IMPRESION",
    ],
    "Rollo bilaminado con impresión": [
        "ROLLO LAMINADO-1600-BI",
    ],
    "Rollo trilaminado sin impresión": [
        "ROLLO LAMINADO-1600-TRI- SIN IMPRESIÓN",
    ],
    "Rollo trilaminado con impresión": [
        "ROLLO LAMINADO-1600-TRI",
    ],
    
}
Tipo_Bobinado: list = [
"Tubular",
"Semitubular",
"Lámina",
"Lámina doble",
]

Acabado: list = [
"Grafilado",
"Liso",
"Macro Perforado",
"Micro Perforado",
]

Tratado: list = [
"SIN TRATAR",
"TRATADO 1 CARA",
"TRATADO 2 CARAS",   
]
Numero_Bobinado: list = [
   "1",
   "2",
   "3",
   "4",
   "5",
   "6",
   "7",
   "8",
   "9",
   "10",
   "11",
   "12",
   "13",
   "14",
   "15",
   "16",
   "17",
   "18",
   "19",
   "20",
   "21",
   "22",
   "23",
   "24"
]

# Configuración base para todos los campos
valor_exepcional = {
    "Material_2": True,
    "Material_3": True,
    "Color": True,
    "Numero_bobinado": True,
    "Fuelle_izquierdo": True,
    "Fuelle_derecho": True,
    "Acabado": True,
    "Tratado": True,
}

# Diccionario para almacenar configuraciones por tipo de producto
campos_por_tipo = {}

# Excepciones por tipo de producto
excepciones_por_tipo = {
     "Rollo sin impresión": ["Material_2", "Material_3", "Color",  "Numero_bobinado"],
     "Rollo con impresión": ["Material_2", "Material_3"],
 }

# Excepciones por grupo específico
excepciones_por_grupo = {
    "Fuelle_izquierdo": [
        "ROLLO PEBD TERMOENCOGIBLE-SIN IMPRESION-1107",
        "ROLLO STRETCH-SIN IMPRESION-1112",
        "ROLLO SIN FIN PEBD ORIGINAL-SIN IMPRESION-1401",
        "ROLLO CENEFA PEBD ORIGINAL-SIN IMPRESION-1501",
    ],
    "Fuelle_derecho": [
        "ROLLO PEBD TERMOENCOGIBLE-SIN IMPRESION-1107",
        "ROLLO MOPP-SIN IMPRESION-1108",
        "ROLLO BOPP-SIN IMPRESION-1109",
        "ROLLO CASTPP-SIN IMPRESION-1111",
        "ROLLO STRETCH-SIN IMPRESION-1112",
    ],
    "Acabado": [
        "ROLLO STRETCH-SIN IMPRESION-1112",
    ],
    "Tratado": [
        "ROLLO STRETCH-SIN IMPRESION-1112",
        "ROLLO PEBD ANCHO-SIN IMPRESION-1120",
        "ROLLO PEBD CORRIENTE ANCHO-SIN IMPRESION-1121",
    ],
   
}

# Generar configuraciones base para todos los tipos y grupos
for tipo_producto, grupos in Grupos_por_Tipo_Producto.items():
    campos_por_tipo[tipo_producto] = {}
    for grupo in grupos:
        # Inicia cada grupo con la configuración base
        campos_por_tipo[tipo_producto][grupo] = valor_exepcional.copy()

# Aplicar excepciones por tipo de producto
for tipo_producto, campos in excepciones_por_tipo.items():
     if tipo_producto in campos_por_tipo:
         for grupo in campos_por_tipo[tipo_producto]:
             for campo in campos:
                campos_por_tipo[tipo_producto][grupo][campo] = False

# Aplicar excepciones por grupo
for campo, grupos in excepciones_por_grupo.items():
    for tipo_producto, grupos_tipo in campos_por_tipo.items():
        for grupo in grupos_tipo:
            if grupo in grupos:
                campos_por_tipo[tipo_producto][grupo][campo] = False

# # Resultado final
# import pprint
# pprint.pprint(campos_por_tipo)

























# valor_exepcional = {
#     "color": False,
#     "numero_bobinado": False,
#     "fuelle_izquierdo": True,
#     "fuelle_derecho": True,
#     "acabado": True,
#     "tratado": True,
#     "Material_2":False,
#     "Material_3":False,
# }

# # Diccionario para almacenar configuraciones por tipo de producto
# campos_por_tipo = {}

# # Generar configuraciones base para todos los grupos
# for tipo_producto, grupos in Grupos_por_Tipo_Producto.items():
#     campos_por_tipo[tipo_producto] = {}
#     for grupo in grupos:
#         campos_por_tipo[tipo_producto][grupo] = valor_exepcional.copy()

# # Aplicar excepciones específicas
# # Excepciones para "Rollo sin impresión"
# campos_por_tipo["Rollo sin impresión"]["ROLLO STRETCH-SIN IMPRESION-1112"]["acabado"] = False
# campos_por_tipo["Rollo sin impresión"]["ROLLO STRETCH-SIN IMPRESION-1112"]["tratado"] = False
# campos_por_tipo["Rollo sin impresión"]["ROLLO PEBD TERMOENCOGIBLE-SIN IMPRESION-1107"]["fuelle_derecho"] = False
# campos_por_tipo["Rollo sin impresión"]["ROLLO MOPP-SIN IMPRESION-1108"]["fuelle_derecho"] = False
# campos_por_tipo["Rollo sin impresión"]["ROLLO BOPP-SIN IMPRESION-1109"]["fuelle_derecho"] = False
# campos_por_tipo["Rollo sin impresión"]["ROLLO CASTPP-SIN IMPRESION-1111"]["fuelle_derecho"] = False
# campos_por_tipo["Rollo sin impresión"]["ROLLO SIN FIN PEBD ORIGINAL-SIN IMPRESION-1401"]["fuelle_izquierdo"] = False
# campos_por_tipo["Rollo sin impresión"]["ROLLO CENEFA PEBD ORIGINAL-SIN IMPRESION-1501"]["fuelle_izquierdo"] = False

# # Excepciones para "Rollo con impresión"
# # (Ejemplo: Añadir si hay configuraciones específicas)
# campos_por_tipo["Rollo con impresión"]["ROLLO PEBD ORIGINAL-1101"]["tratado"] = True
