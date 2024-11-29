#aca es donde nacen las referencias les daremos sus respectivos oredenes y valores

# Diccionario único para el campo "material"
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
    "materia_1": MATERIAL,
    "material_2": MATERIAL,  
    "material_3": MATERIAL,  
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
    "unidades_ancho": {
        "Centímetros": "cm",
        "Milímetros": "mm",
        "Pulgadas": "in",
    },
    "unidades_largo": {
        "Centímetros": "cm",
        "Milímetros": "mm",
        "Pulgadas": "in",
        "Metros": "m",
    },
    "unidades_calibre": {
        "Milésimas de pulgada": "mils",
        "Micras": "mic",
    },
    "tipo_bobinado": {
        "Tubular": "TUB",
        "Semitubular": "STUB",
        "Lámina": "LAM",
        "Lámina doble": "LAM_DOB",
    },
    "acabado": {
        "Grafilado": "GRAF",
        "Liso": "LISO",
        "Macro Perforado": "MAC_Perf",
        "Micro Perforado": "MIC_Perf",
    },
    "tratado": {
        "Sin tratar": "ST",
        "Tratado 1 cara": "T1C",
        "Tratado 2 caras": "T2C",
    },
}

ORDEN_CAMPOS = [
    "tipo_producto",  # Campo fijo: Tipo de producto
    "R*",             # Literal fijo
    "Material",# Literal adicional o campo
    "Grupo",
    "color",          # Color del producto
    "ancho",          # Ancho del producto
    "unidades_ancho", # Unidades del ancho (cm, mm, in)
    "*",              # Separador fijo
    "calibre",        # Calibre del producto
    "unidades_calibre", # Unidades del calibre (mils, mic)
    "*",              # Separador fijo
    "largo",          # Largo del producto
    "unidades_largo", # Unidades del largo (cm, mm, m, in)
    "tipo_bobinado",  # Tipo de bobinado (Tubular, Semitubular, etc.)
    "Ref",            # Literal fijo
    "referencia",     # La referencia generada
]
