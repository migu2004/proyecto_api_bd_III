from pydantic import BaseModel
from datetime import datetime

class InscripcionCreate(BaseModel):
    estudiante_id: str
    curso_id: str

class InscripcionResponse(InscripcionCreate):
    id: str
    fecha_inscripcion: datetime