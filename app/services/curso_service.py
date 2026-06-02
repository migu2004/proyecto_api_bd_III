from bson import ObjectId
from app.database import cursos_collection
from app.models.pyobjectid import curso_helper


async def crear(curso_data: dict) -> dict:
    nuevo = await cursos_collection.insert_one(curso_data)
    created = await cursos_collection.find_one({"_id": nuevo.inserted_id})
    return curso_helper(created)


async def listar() -> list:
    cursos = []
    async for curso in cursos_collection.find():
        cursos.append(curso_helper(curso))
    return cursos


async def buscar(filtro: dict) -> list:
    cursos = []
    async for curso in cursos_collection.find(filtro):
        cursos.append(curso_helper(curso))
    return cursos


async def obtener_por_id(id: str) -> dict | None:
    if not ObjectId.is_valid(id):
        return None
    curso = await cursos_collection.find_one({"_id": ObjectId(id)})
    return curso_helper(curso) if curso else None


async def actualizar(id: str, curso_data: dict) -> dict | None:
    if not ObjectId.is_valid(id):
        return None
    result = await cursos_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": curso_data}
    )
    if result.modified_count == 0:
        return None
    updated = await cursos_collection.find_one({"_id": ObjectId(id)})
    return curso_helper(updated)


async def eliminar(id: str) -> bool:
    if not ObjectId.is_valid(id):
        return False
    result = await cursos_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1
