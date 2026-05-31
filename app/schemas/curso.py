from pydantic import BaseModel, Field
from typing import Optional

class CursoBase(BaseModel):
    titulo: str = Field(..., example="Introducción a FastAPI")
    categoria: str = Field(..., example="Programación")
    instructor: str = Field(..., example="Profesor Turing")
    duracion_horas: int = Field(..., example=20)
    activo: bool = Field(default=True)

class CursoCreate(CursoBase):
    pass

class CursoResponse(CursoBase):
    id: str

    class Config:
        from_attributes = True