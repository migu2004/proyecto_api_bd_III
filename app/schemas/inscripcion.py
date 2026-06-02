from pydantic import BaseModel, ConfigDict
from datetime import datetime

class InscripcionCreate(BaseModel):
    estudiante_id: str
    curso_id: str

class InscripcionResponse(InscripcionCreate):
    id: str
    fecha_inscripcion: datetime
    model_config = ConfigDict(from_attributes=True)
