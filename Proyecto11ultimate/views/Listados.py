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

Tipo_Producto_Rollos: list = [
    "Rollo sin impresión", 
    "Rollo con impresión", 
    "Rollo bilaminado sin impresión", 
    "Rollo bilaminado con impresión", 
    "Rollo trilaminado sin impresión", 
    "Rollo trilaminado con impresión", 
    "Plástico para invernadero",
    "Rollo acolchado/mulch", 
    
]
Tipos_Productos_Bolsas: list =[
    "Bolsa con Impresión",
    "otros",
]
#preguntar si estan bien las unidades de esta manera 
Unidades_Ancho: list[str] = [
"Centímetros(cm)",
"Milímetros(mm)",
"Pulgadas(in)",

]
Unidades_Largo: list = [
"Centímetros(cm)",
"Milímetros(mm)",
"Pulgadas(in)",
"Metros(m)",
  
]
Unidades_Calibre: list = [
 "Milésimas de pulgada(mils)",
 "Micras(mic)",  
]
Tipo_Bobinado: list = [
"Tubular",
"Semitubular",
"Lámina",
"Lámina doble",
"Total Lamina",
]

Acabado: list = [
"Grafilado",
"Liso",
"Macro Perforado",
"Micro Perforado",
"Precorte",
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
Tipo_Bolsa: list = [
    "Doy pack",
    "Flow Pack-selle inferior",
    "Flow Pack-selle superior",
    "Estándar",
    "Selles planos"
]

Tipo_Selle: list = [
    "2 sellés planos",
    "3 selles planos",
    "4 selles planos",
    "Camiseta",
    "Corte",
    "Doble fondo",
    "Fondo",
    "Lateral",
    "Precorte"
]

Tipo_Troquel: list = [
    "Banana",
    "Camiseta",
    "Circular 5mm",
    "Circular 8mm",
    "Eurohole",
    "Circular 30mm"
]
Tipo_Solapa: list = [
    "Solapa Doble Interna",
    "Solapa Externa",
    "Solapa Interna"
]

Grupos_por_Tipo_Producto =  {
    "Rollo sin impresión": [
        "ROLLO PEBD ORIGINAL-S.I-1101",
        "ROLLO PEBD CORRIENTE-S.I-1102",
        "ROLLO PEBD SEMIORIGINAL-S.I-1103",
        "ROLLO PEBD COEXTRUIDO-S.I-1104",
        "ROLLO PEAD ORIGINAL-S.I-1105",
        "ROLLO PEAD CORRIENTE-S.I-1106",
        "ROLLO PEBD TERMOENCOGIBLE-S.I-1107",
        "ROLLO MOPP-S.I-1108",
        "ROLLO BOPP-S.I-1109",
        "ROLLO CASTPP-S.I-1111",
        "ROLLO STRETCH-S.I-1112",
        "ROLLO NEGRO SEMIORIGINAL-S.I-1122",
        "ROLLO PEBD ANCHO-S.I-1120",
        "ROLLO PEBD CORRIENTE ANCHO-S.I-1121",
        "ROLLO SIN FIN PEBD ORIGINAL-S.I-1401",
        "ROLLO CENEFA PEBD ORIGINAL-S.I-1501",
    ],
    "Rollo con impresión": [
        "ROLLO PEBD ORIGINAL-C.I-1101",
        "ROLLO PEBD CORRIENTE-C.I-1102",
        "ROLLO PEBD SEMIORIGINAL-C.I-1103",
        "ROLLO PEBD COEXTRUIDO-C.I-1104",
        "ROLLO PEAD ORIGINAL-C.I-1105",
        "ROLLO PEAD CORRIENTE-C.I-1106",
        "ROLLO MOPP-C.I-1108",
        "ROLLO BOPP-C.I-1109",
        "ROLLO CASTPP-C.I-1111",
        "ROLLO NEGRO SEMIORIGINAL-C.I-1122",
        "ROLLO SIN FIN PEBD ORIGINAL-C.I-1401",
        "ROLLO CENEFA PEBD ORIGINAL-C.I-1501",
    ],
    "Rollo bilaminado sin impresión": [
        "ROLLO LAMINADO-1600-BI-S.I",
    ],
    "Rollo bilaminado con impresión": [
        "ROLLO LAMINADO-1600-BI.C.I",
    ],
    "Rollo trilaminado sin impresión": [
        "ROLLO LAMINADO-1600-TRI-S.I",
    ],
    "Rollo trilaminado con impresión": [
        "ROLLO LAMINADO-1600-TRI-C.I",
    ],
    "Plástico para invernadero":[
        "ROLLO PROVIAGRO ENERGY-1114",
        "ROLLO PROVIAGRO LUMINANCE-1115",
        "ROLLO PROVIAGRO SPECTRUM-1116",
        "ROLLO PROVIAGRO CLOUDY-1117",
        "ROLLO PROVIAGRO BLACK-1118",
    ],
    "Rollo acolchado/mulch":[
       "ROLLO PROVIAGRO MULCH-1119",
    ],

    #BOLSAS
    "Bolsa con Impresión":[
        "BOLSA PEBD ORIGINAL - 1201",
        "BOLSA PEBD CORRIENTE-1202",
        "BOLSA PEAD ORIGINAL-1205",
        "BOLSA MOPP-1208",
    ]
    
}

Valores_predeterminados = {
    "ROLLO PEBD TERMOENCOGIBLE-S.I-1107":{
         "Color":"Transparente",
     },
     "ROLLO MOPP-S.I-1108":{
         "Color":"Transparente",
     },
     "ROLLO STRETCH-S.I-1112":{
         "Color":"Transparente",
     },

     "ROLLO PROVIAGRO ENERGY-1114":{
         "Material_1":"Polietileno de Baja Densidad",
         "Unidades_Calibre":"Milésimas de pulgada(mils)",
         "Unidades_Largo":"Metros(m)",   
     },

     "ROLLO PROVIAGRO LUMINANCE-1115":{
        "Material_1":"Polietileno de Baja Densidad",
         "Unidades_Calibre":"Milésimas de pulgada(mils)",
         "Unidades_Largo":"Metros(m)",    
     },
     "ROLLO PROVIAGRO SPECTRUM-1116":{
       "Material_1":"Polietileno de Baja Densidad",
        "Unidades_Calibre":"Milésimas de pulgada(mils)",
        "Unidades_Largo":"Metros(m)",    
     },
     "ROLLO PROVIAGRO CLOUDY-1117":{
        "Material_1":"Polietileno de Baja Densidad",
         "Unidades_Calibre":"Milésimas de pulgada(mils)",
         "Unidades_Largo":"Metros(m)",   
     },
      "ROLLO PROVIAGRO BLACK-1118":{
         "Material_1":"Polietileno de Baja Densidad",
          "Unidades_Calibre":"Milésimas de pulgada(mils)",
          "Unidades_Largo":"Metros(m)",   
      },
      "ROLLO PROVIAGRO MULCH-1119":{
         "Material_1":"Polietileno de Baja Densidad",
          "Unidades_Calibre":"Milésimas de pulgada(mils)", 
          "Unidades_Largo":"Metros(m)",   
      },      
     }   
 


# Configuración base para todos los campos
valor_exepcional = {
    "Material_1":True,
    "Material_2": True,
    "Material_3": True,
    "Color": True,
    "Peso_Estructura":True,
    "Numero_Bobinado": True,
    "Fuelle_izquierdo": True,
    "Fuelle_derecho": True,
    "Acabado": True,
    "Tratado": True,
}

# Diccionario para almacenar configuraciones por tipo de producto
Campos_por_Tipo = {}

# Excepciones por tipo de producto
excepciones_por_tipo = {
     "Rollo sin impresión": ["Material_2", "Material_3","Numero_Bobinado"],
     "Rollo con impresión": ["Material_2", "Material_3","Acabado"],
     "Plástico para invernadero":["Material_2", "Material_3", "Peso_Estructura", "Numero_Bobinado", "Acabado", "Tratado"],
     "Rollo acolchado/mulch":["Peso_Estructura", "Numero_Bobinado", "Acabado", "Tratado"],
     
 }

# Excepciones por grupo específico
excepciones_rollos = {
    "Fuelle_izquierdo": [
        "ROLLO PEBD TERMOENCOGIBLE-S.I-1107",
        "ROLLO STRETCH-S.I-1112",
        "ROLLO SIN FIN PEBD ORIGINAL-S.I-1401",
        "ROLLO CENEFA PEBD ORIGINAL-S.I-1501",
        "ROLLO MOPP-C.I-1108",
        "ROLLO BOPP-C.I-1109",
        "ROLLO SIN FIN PEBD ORIGINAL-C.I-1401",
        "ROLLO CENEFA PEBD ORIGINAL-C.I-1501",
        "ROLLO LAMINADO-1600-BI-S.I",
        "ROLLO LAMINADO-1600-BI.C.I",
        "ROLLO LAMINADO-1600-TRI-S.I",
        "ROLLO LAMINADO-1600-TRI-C.I",
    ],
    "Fuelle_derecho": [
        "ROLLO PEBD TERMOENCOGIBLE-S.I-1107",
        "ROLLO MOPP-S.I-1108",
        "ROLLO BOPP-S.I-1109",
        "ROLLO CASTPP-S.I-1111",
        "ROLLO STRETCH-S.I-1112",
        "ROLLO SIN FIN PEBD ORIGINAL-S.I-1401",
        "ROLLO CENEFA PEBD ORIGINAL-S.I-1501",
        "ROLLO MOPP-C.I-1108",
        "ROLLO BOPP-C.I-1109",
        "ROLLO SIN FIN PEBD ORIGINAL-C.I-1401",
        "ROLLO CENEFA PEBD ORIGINAL-C.I-1501",
        "ROLLO LAMINADO-1600-BI-S.I",
        "ROLLO LAMINADO-1600-BI.C.I",
        "ROLLO LAMINADO-1600-TRI-S.I",
        "ROLLO LAMINADO-1600-TRI-C.I",
    ],
    "Acabado": [
        "ROLLO STRETCH-S.I-1112",
        "ROLLO PEBD TERMOENCOGIBLE-S.I-1107",
        "ROLLO LAMINADO-1600-BI-S.I",
        "ROLLO LAMINADO-1600-BI.C.I",
        "ROLLO LAMINADO-1600-TRI-S.I",
        "ROLLO LAMINADO-1600-TRI-C.I",
        "ROLLO PEBD ANCHO-S.I-1120",
        "ROLLO PEBD CORRIENTE ANCHO-S.I-1121",
    ],
    "Tratado": [
        "ROLLO PEBD TERMOENCOGIBLE-S.I-1107",
        "ROLLO STRETCH-S.I-1112",
        "ROLLO PEBD ANCHO-S.I-1120",
        "ROLLO PEBD CORRIENTE ANCHO-S.I-1121",
        "ROLLO LAMINADO-1600-BI-S.I",
        "ROLLO LAMINADO-1600-BI.C.I",
        "ROLLO LAMINADO-1600-TRI-S.I",
        "ROLLO LAMINADO-1600-TRI-C.I",
        "ROLLO LAMINADO-1600-TRI-C.I",
        
    ],
    "Color":[
    #    "ROLLO PEBD ORIGINAL-S.I-1101",
    #     "ROLLO PEBD CORRIENTE-S.I-1102",
    #     "ROLLO PEBD SEMIORIGINAL-S.I-1103",
    #     "ROLLO PEBD COEXTRUIDO-S.I-1104",
    #     "ROLLO PEAD ORIGINAL-S.I-1105",
    #     "ROLLO PEAD CORRIENTE-S.I-1106",
    #     "ROLLO BOPP-S.I-1109",
    #     "ROLLO CASTPP-S.I-1111",
    #     "ROLLO NEGRO SEMIORIGINAL-S.I-1122",
    #     "ROLLO PEBD ANCHO-S.I-1120",
    #     "ROLLO PEBD CORRIENTE ANCHO-S.I-1121",
    #     "ROLLO SIN FIN PEBD ORIGINAL-S.I-1401",
    #     "ROLLO CENEFA PEBD ORIGINAL-S.I-1501",
        "ROLLO MOPP-C.I-1108",  
    ],
    "Numero_Bobinado":[
       "ROLLO LAMINADO-1600-BI-S.I",
       "ROLLO LAMINADO-1600-TRI-S.I",
    ],
    "Material_2":[
      "ROLLO PROVIAGRO MULCH-1119",
      "BOLSA PEBD ORIGINAL - 1201",
     "BOLSA PEBD CORRIENTE-1202",
     "BOLSA PEAD ORIGINAL-1205",  
    ],
    "Material_3":[
        "ROLLO PROVIAGRO MULCH-1119",
        "ROLLO LAMINADO-1600-BI-S.I",
        "ROLLO LAMINADO-1600-BI.C.I",
        "BOLSA PEBD ORIGINAL - 1201",
        "BOLSA PEBD CORRIENTE-1202",
        "BOLSA PEAD ORIGINAL-1205",

    ],
   
}

# Generar configuraciones base para todos los tipos y grupos
for tipo_producto, grupos in Grupos_por_Tipo_Producto.items():
    Campos_por_Tipo[tipo_producto] = {}
    for grupo in grupos:
        # Inicia cada grupo con la configuración base
        Campos_por_Tipo[tipo_producto][grupo] = valor_exepcional.copy()

# Aplicar excepciones por tipo de producto
for tipo_producto, campos in excepciones_por_tipo.items():
     if tipo_producto in Campos_por_Tipo:
         for grupo in Campos_por_Tipo[tipo_producto]:
             for campo in campos:
                Campos_por_Tipo[tipo_producto][grupo][campo] = False

# Aplicar excepciones por grupo
for campo, grupos in excepciones_rollos.items():
    for tipo_producto, grupos_tipo in Campos_por_Tipo.items():
        for grupo in grupos_tipo:
            if grupo in grupos:
                Campos_por_Tipo[tipo_producto][grupo][campo] = False

                

# # Aplicar valores predeterminados
# for grupo, campos in valores_predeterminados.items():
#     for tipo_producto, grupos_tipo in Campos_por_Tipo.items():
#         if grupo in grupos_tipo:
#             for campo, valor in campos.items():
#                 if campo in Campos_por_Tipo[tipo_producto][grupo]:
#                     Campos_por_Tipo[tipo_producto][grupo][campo] = valor

# # Resultado final
# import pprint
  
# pprint.pprint(Campos_por_Tipo)

























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
