import reflex as rx 



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
        "Centímetros(cm)": "cm",
        "Milímetros(mm)": "mm",
        "Pulgadas(in)": "in",
    },
    "Unidades_Largo": {
        "Centímetros(cm)": "cm",
        "Milímetros(mm)": "mm",
        "Pulgadas(in)": "in",
        "Metros(m)": "m",
    },
    "Unidades_Calibre": {
        "Milésimas de pulgada(mils)": "mils",
        "Micras(mic)": "mic",
    },
    "Tipo_Bobinado": {
        "Tubular": "TUB",
        "Semitubular": "STUB",
        "Lámina": "LAM",
        "Lámina doble": "LAM_DOB",
        "Total Lamina": "T-LAM"

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
        "TRATADO 2 CARAS": "T2C",
    },
}

LITERALES_FIJOS = {
    "Unidades_Ancho": "*",
    "Unidades_Calibre": "*",
    "Fuelle_Izquierdo": "+",
    "Fuelle_Derecho": "+",
    #"Referencia": "Ref",
}

Grupos_Especiales = {
    "ROLLO PEBD CORRIENTE-S.I-1102": "Cte",
    "ROLLO PEBD SEMIORIGINAL-S.I-1103": "SemiOrg",
    "ROLLO PEBD COEXTRUIDO-S.I-1104": "Coext",
    "ROLLO PEAD CORRIENTE-S.I-1106": "Cte",
    "ROLLO PEBD TERMOENCOGIBLE-S.I-1107": "Termoenc",
    "ROLLO NEGRO SEMIORIGINAL-S.I-1122": "SemiOrg",
    "ROLLO PEBD CORRIENTE-C.I-1102": "Cte",
    "ROLLO PEBD SEMIORIGINAL-C.I-1103": "SemiOrg",
    "ROLLO PEBD COEXTRUIDO-C.I-1104": "Coext",
    "ROLLO PEAD CORRIENTE-C.I-1106": "Coext",
    "ROLLO NEGRO SEMIORIGINAL-C.I-1122": "SemiOrg",

    
}
ORDEN_CAMPOS_ROLLOS = { 
    #"Tipo_Producto": False,  
    "R-": True,
    "Material_1": False,
    "ESPACIO_0": "False",
    "Literal_Especial": False,
    "ESPACIO_1": True,
    "Color": False,
    "ESPACIO_2": True,
    "Ancho": False,
    #"ESPACIO_3": True,  # Espacio después del ancho
    "Fuelle_Izquierdo": False,
    "Fuelle_Derecho": False,          
    "Unidades_Ancho": False,             
    "Calibre": False,        
    "Unidades_Calibre": False,        
    "Largo": False,          
    "Unidades_Largo": False,
    "ESPACIO_4": True,
    "Tratado": False,
    "ESPACIO_5": True,  
    "Acabado": False,
    "ESPACIO_6": True,
    "Tipo_Bobinado": False,     
    #"Ref": False,
    "ESPACIO_7": True,           
    "Referencia": False,
    "ESPACION_8":True,
    
    
}
