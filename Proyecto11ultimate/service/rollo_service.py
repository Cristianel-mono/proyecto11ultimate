from ..backend.metodosdb import select_rollo
#aaca se pone la logica del negocio

def select_all_rollo_service():
    rollos =  select_rollo()
    print(rollos)
    return rollos