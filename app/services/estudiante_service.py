from datetime import datetime, timezone
from bson import ObjectId
from app.database import estudiantes_collection
from app.models.pyobjectid import estudiante_helper


async def crear(estudiante_data: dict) -> dict:
    estudiante_data["fecha_registro"] = datetime.now(timezone.utc)
    nuevo = await estudiantes_collection.insert_one(estudiante_data)
    created = await estudiantes_collection.find_one({"_id": nuevo.inserted_id})
    return estudiante_helper(created)


async def listar() -> list:
    estudiantes = []
    async for estudiante in estudiantes_collection.find():
        estudiantes.append(estudiante_helper(estudiante))
    return estudiantes


async def obtener_por_id(id: str) -> dict | None:
    if not ObjectId.is_valid(id):
        return None
    estudiante = await estudiantes_collection.find_one({"_id": ObjectId(id)})
    return estudiante_helper(estudiante) if estudiante else None


async def actualizar(id: str, estudiante_data: dict) -> dict | None:
    if not ObjectId.is_valid(id):
        return None
    result = await estudiantes_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": estudiante_data}
    )
    if result.modified_count == 0:
        return None
    updated = await estudiantes_collection.find_one({"_id": ObjectId(id)})
    return estudiante_helper(updated)


async def eliminar(id: str) -> bool:
    if not ObjectId.is_valid(id):
        return False
    result = await estudiantes_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1
