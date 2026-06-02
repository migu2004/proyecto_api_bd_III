from pydantic import BaseModel, Field, ConfigDict

class CursoBase(BaseModel):
    titulo: str = Field(..., json_schema_extra={"example": "Introducción a FastAPI"})
    categoria: str = Field(..., json_schema_extra={"example": "Programación"})
    instructor: str = Field(..., json_schema_extra={"example": "Profesor Turing"})
    duracion_horas: int = Field(..., json_schema_extra={"example": 20})
    activo: bool = Field(default=True)

class CursoCreate(CursoBase):
    pass

class CursoResponse(CursoBase):
    id: str
    model_config = ConfigDict(from_attributes=True)
