from fastapi import FastAPI
from app.routes.cursos import router as cursos_router
from app.routes.estudiantes import router as estudiantes_router
from app.routes.inscripciones import router as inscripciones_router

app = FastAPI(
    title="API de Plataforma de Cursos",
    description="API REST funcional conectada a MongoDB para gestión de cursos, estudiantes e inscripciones",
    version="1.0.0"
)

app.include_router(cursos_router)
app.include_router(estudiantes_router)
app.include_router(inscripciones_router)


@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de la Plataforma de Cursos. Visita /docs para interactuar."}