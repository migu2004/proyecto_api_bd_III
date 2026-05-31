from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

# Colecciones requeridas
cursos_collection = db["cursos"]
estudiantes_collection = db["estudiantes"]
inscripciones_collection = db["inscripciones"]