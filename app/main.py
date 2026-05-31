# app/main.py
from fastapi import FastAPI
from app.routes.cursos import router as cursos_router

app = FastAPI(
    title="API de Plataforma de Cursos",
    description="API REST funcional conectada a MongoDB para gestión de cursos",
    version="1.0.0"
)

# Incluir las rutas del recurso
app.include_router(cursos_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de la Plataforma de Cursos. Visita /docs para interactuar."}