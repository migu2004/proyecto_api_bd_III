from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from app.schemas.inscripcion import InscripcionCreate, InscripcionResponse
from app.services.inscripcion_service import crear, listar, obtener_por_id, eliminar
from app.services.curso_service import obtener_por_id as curso_por_id
from app.services.estudiante_service import obtener_por_id as estudiante_por_id

router = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])


@router.post("/", response_model=InscripcionResponse, status_code=status.HTTP_201_CREATED)
async def crear_inscripcion(inscripcion: InscripcionCreate):
    if not ObjectId.is_valid(inscripcion.estudiante_id):
        raise HTTPException(status_code=400, detail="ID de estudiante inválido")
    if not ObjectId.is_valid(inscripcion.curso_id):
        raise HTTPException(status_code=400, detail="ID de curso inválido")

    estudiante = await estudiante_por_id(inscripcion.estudiante_id)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    curso = await curso_por_id(inscripcion.curso_id)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")

    return await crear(inscripcion.model_dump())


@router.get("/", response_model=List[InscripcionResponse])
async def listar_inscripciones():
    return await listar()


@router.get("/{id}", response_model=InscripcionResponse)
async def obtener_inscripcion(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    insc = await obtener_por_id(id)
    if insc is None:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return insc


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_inscripcion(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    deleted = await eliminar(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return
