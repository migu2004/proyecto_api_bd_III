from fastapi import APIRouter, HTTPException, status, Query
from bson import ObjectId
from app.database import cursos_collection
from app.schemas.curso import CursoCreate, CursoResponse
from app.models.pyobjectid import curso_helper
from typing import List

router = APIRouter(prefix="/cursos", tags=["Cursos"])

# Crear un registro
@router.post("/", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
async def crear_curso(curso: CursoCreate):
    nuevo_curso = await cursos_collection.insert_one(curso.model_dump())
    created_curso = await cursos_collection.find_one({"_id": nuevo_curso.inserted_id})
    return curso_helper(created_curso)

# Listar registros
@router.get("/", response_model=List[CursoResponse])
async def listar_cursos():
    cursos = []
    async for curso in cursos_collection.find():
        cursos.append(curso_helper(curso))
    return cursos

# GET /recurso/buscar?... (Consulta adicional por filtro)
@router.get("/buscar", response_model=List[CursoResponse])
async def buscar_cursos(
    categoria: str = Query(None, description="Filtrar por categoría del curso"),
    solo_activos: bool = Query(None, description="Filtrar solo cursos activos")
):
    query = {}
    if categoria:
        query["categoria"] = categoria
    if solo_activos is not None:
        query["activo"] = solo_activos

    cursos = []
    async for curso in cursos_collection.find(query):
        cursos.append(curso_helper(curso))
    return cursos

# GET /recurso/{id} (Consultar un registro por id)
@router.get("/{id}", response_model=CursoResponse)
async def obtener_curso(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    curso = await cursos_collection.find_one({"_id": ObjectId(id)})
    if curso:
        return curso_helper(curso)
    raise HTTPException(status_code=404, detail="Curso no encontrado")

# PUT /recurso/{id} (Actualizar un registro)
@router.put("/{id}", response_model=CursoResponse)
async def actualizar_curso(id: str, curso: CursoCreate):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    update_result = await cursos_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": curso.model_dump()}
    )
    if update_result.modified_count == 1:
        updated_curso = await cursos_collection.find_one({"_id": ObjectId(id)})
        return curso_helper(updated_curso)
    raise HTTPException(status_code=404, detail="Curso no encontrado o sin cambios")

# DELETE /recurso/{id} (Eliminar un registro)
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_curso(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    delete_result = await cursos_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return
    raise HTTPException(status_code=404, detail="Curso no encontrado")

