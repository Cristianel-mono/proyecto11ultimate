from sqlmodel import create_engine
import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("")
#firebase_admin.initialize_app(cred)

db = firestore.client()

def connect():
    engine = create_engine(cred)
