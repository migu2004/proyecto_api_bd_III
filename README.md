# API - Plataforma de Cursos (FastAPI + MongoDB)

Este proyecto es una API RESTful desarrollada con FastAPI y conectada a MongoDB para gestionar una Plataforma de Cursos. Incluye operaciones CRUD completas y consultas especializadas.

## Requisitos previos
* Python 3.10+
* MongoDB instalado y ejecutándose localmente (puerto 27017) o conexión a MongoDB Atlas.

## Instrucciones de ejecución

1. **Crear y activar el entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # En Windows: venv\Scripts\activate
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno:**
   Editar el archivo `.env` con la URI de MongoDB y el nombre de la base de datos:
   ```
   MONGO_URI=mongodb://localhost:27017
   MONGO_DB_NAME=plataforma_cursos
   ```

4. **Ejecutar la aplicación:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Acceder a la documentación interactiva:**
   - Swagger UI: http://localhost:8000/docs
   - Redoc: http://localhost:8000/redoc

## Endpoints disponibles

### Cursos
| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/cursos/` | Crear un nuevo curso |
| GET | `/cursos/` | Listar todos los cursos |
| GET | `/cursos/buscar` | Buscar cursos por categoría y/o estado activo |
| GET | `/cursos/{id}` | Obtener un curso por ID |
| PUT | `/cursos/{id}` | Actualizar un curso por ID |
| DELETE | `/cursos/{id}` | Eliminar un curso por ID |

### Estudiantes
| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/estudiantes/` | Crear un nuevo estudiante |
| GET | `/estudiantes/` | Listar todos los estudiantes |
| GET | `/estudiantes/{id}` | Obtener un estudiante por ID |
| PUT | `/estudiantes/{id}` | Actualizar un estudiante por ID |
| DELETE | `/estudiantes/{id}` | Eliminar un estudiante por ID |

### Inscripciones
| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/inscripciones/` | Inscribir un estudiante en un curso |
| GET | `/inscripciones/` | Listar todas las inscripciones |
| GET | `/inscripciones/{id}` | Obtener una inscripción por ID |
| DELETE | `/inscripciones/{id}` | Eliminar una inscripción |

## Tecnologías utilizadas

- **FastAPI** — Framework web asíncrono
- **Motor** — Driver asíncrono para MongoDB
- **Pydantic** — Validación de datos y settings
- **Uvicorn** — Servidor ASGI

## Ejecutar tests

```bash
source venv/bin/activate
pytest tests/ -v
```
