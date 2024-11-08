from ..backend.metodosdb import select_all


def select_all_rollo_service():
    rollos =  select_all()
    print(rollos)
    return rollos