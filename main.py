from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

# 🔹 Pega aquí tu conexión de MongoDB
MONGO_URI = "mongodb+srv://<db_username>:<db_password>@cluster0.vzr9qw6.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client.iot
collection = db.sensores

# Ruta de prueba
@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

# Ruta para guardar datos
@app.post("/sensor")
def guardar_sensor(data: dict):
    data["fecha"] = datetime.now()
    collection.insert_one(data)
    return {"status": "dato guardado"}


