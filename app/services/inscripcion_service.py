from datetime import datetime, timezone
from bson import ObjectId
from app.database import inscripciones_collection
from app.models.pyobjectid import inscripcion_helper


async def crear(inscripcion_data: dict) -> dict:
    inscripcion_data["fecha_inscripcion"] = datetime.now(timezone.utc)
    nuevo = await inscripciones_collection.insert_one(inscripcion_data)
    created = await inscripciones_collection.find_one({"_id": nuevo.inserted_id})
    return inscripcion_helper(created)


async def listar() -> list:
    inscripciones = []
    async for insc in inscripciones_collection.find():
        inscripciones.append(inscripcion_helper(insc))
    return inscripciones


async def obtener_por_id(id: str) -> dict | None:
    if not ObjectId.is_valid(id):
        return None
    insc = await inscripciones_collection.find_one({"_id": ObjectId(id)})
    return inscripcion_helper(insc) if insc else None


async def eliminar(id: str) -> bool:
    if not ObjectId.is_valid(id):
        return False
    result = await inscripciones_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1
