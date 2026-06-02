from unittest.mock import patch, MagicMock, AsyncMock
from fastapi.testclient import TestClient
from app.main import app
from tests.test_cursos import AsyncIter


@patch("app.services.inscripcion_service.inscripciones_collection")
@patch("app.services.curso_service.cursos_collection")
@patch("app.services.estudiante_service.estudiantes_collection")
def test_crear_inscripcion(mock_est, mock_cur, mock_insc):
    mock_est.find_one = AsyncMock(return_value={
        "_id": "est123", "nombre": "Juan", "email": "j@e.com",
        "telefono": None, "fecha_registro": "2024-01-01T00:00:00"
    })
    mock_cur.find_one = AsyncMock(return_value={
        "_id": "cur123", "titulo": "Curso", "categoria": "Prog",
        "instructor": "Profe", "duracion_horas": 10, "activo": True
    })
    mock_insert = MagicMock()
    mock_insert.inserted_id = "insc123"
    mock_insc.insert_one = AsyncMock(return_value=mock_insert)
    mock_insc.find_one = AsyncMock(return_value={
        "_id": "insc123",
        "estudiante_id": "est123",
        "curso_id": "cur123",
        "fecha_inscripcion": "2024-01-01T00:00:00"
    })

    client = TestClient(app)
    response = client.post("/inscripciones/", json={
        "estudiante_id": "507f1f77bcf86cd799439011",
        "curso_id": "507f1f77bcf86cd799439012"
    })

    assert response.status_code == 201
    data = response.json()
    assert data["estudiante_id"] == "est123"
    assert data["curso_id"] == "cur123"


@patch("app.services.inscripcion_service.inscripciones_collection")
def test_listar_inscripciones_vacio(mock_collection):
    mock_collection.find = MagicMock(return_value=AsyncIter([]))

    client = TestClient(app)
    response = client.get("/inscripciones/")
    assert response.status_code == 200
    assert response.json() == []


@patch("app.services.inscripcion_service.inscripciones_collection")
def test_eliminar_inscripcion_ok(mock_collection):
    mock_collection.delete_one = AsyncMock(return_value=MagicMock(deleted_count=1))
    client = TestClient(app)
    response = client.delete("/inscripciones/507f1f77bcf86cd799439011")
    assert response.status_code == 204
