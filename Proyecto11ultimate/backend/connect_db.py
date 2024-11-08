from sqlmodel import create_engine

def connect():
    engine = create_engine("postgresql://postgres:KgGtoJyiCCoHFRAUdLSlOkPKLWErXafh@junction.proxy.rlwy.net:35191/railway")
    return engine












# import firebase_admin
# from firebase_admin import credentials, firestore


# cred = credentials.Certificate("/home/systemas/Documentos/Proyecto11ultimate/credenciales.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()

