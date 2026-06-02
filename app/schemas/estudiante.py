from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class EstudianteBase(BaseModel):
    nombre: str = Field(..., json_schema_extra={"example": "Juan Pérez"})
    email: str = Field(..., json_schema_extra={"example": "juan@email.com"})
    telefono: Optional[str] = Field(None, json_schema_extra={"example": "+54 11 1234-5678"})

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    id: str
    fecha_registro: datetime
    model_config = ConfigDict(from_attributes=True)
