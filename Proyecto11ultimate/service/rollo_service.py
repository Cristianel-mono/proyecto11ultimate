from ..backend.metodosdb import select_rollo
#aaca se pone la logica del negocio
#Aca es donde hacemos las validaciones 
#se crean los metodos que van a interactuar con mi pagina

def select_all_rollo_service():
    rollos =  select_rollo()
    print(rollos)
    return rollos