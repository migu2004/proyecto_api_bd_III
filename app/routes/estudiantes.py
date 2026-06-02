from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from app.schemas.estudiante import EstudianteCreate, EstudianteResponse
from app.services.estudiante_service import (
    crear, listar, obtener_por_id, actualizar, eliminar
)

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


@router.post("/", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED)
async def crear_estudiante(estudiante: EstudianteCreate):
    return await crear(estudiante.model_dump())


@router.get("/", response_model=List[EstudianteResponse])
async def listar_estudiantes():
    return await listar()


@router.get("/{id}", response_model=EstudianteResponse)
async def obtener_estudiante(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    estudiante = await obtener_por_id(id)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante


@router.put("/{id}", response_model=EstudianteResponse)
async def actualizar_estudiante(id: str, estudiante: EstudianteCreate):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    updated = await actualizar(id, estudiante.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado o sin cambios")
    return updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_estudiante(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    deleted = await eliminar(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return
