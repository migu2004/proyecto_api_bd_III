from fastapi import APIRouter, HTTPException, status, Query
from typing import List
from bson import ObjectId
from app.schemas.curso import CursoCreate, CursoResponse
from app.services.curso_service import (
    crear, listar, buscar, obtener_por_id, actualizar, eliminar
)

router = APIRouter(prefix="/cursos", tags=["Cursos"])


@router.post("/", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
async def crear_curso(curso: CursoCreate):
    return await crear(curso.model_dump())


@router.get("/", response_model=List[CursoResponse])
async def listar_cursos():
    return await listar()


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
    return await buscar(query)


@router.get("/{id}", response_model=CursoResponse)
async def obtener_curso(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    curso = await obtener_por_id(id)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


@router.put("/{id}", response_model=CursoResponse)
async def actualizar_curso(id: str, curso: CursoCreate):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    updated = await actualizar(id, curso.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado o sin cambios")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_curso(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    deleted = await eliminar(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return
