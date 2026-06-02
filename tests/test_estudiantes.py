from unittest.mock import patch, MagicMock, AsyncMock
from fastapi.testclient import TestClient
from app.main import app
from tests.test_cursos import AsyncIter


@patch("app.services.estudiante_service.estudiantes_collection")
def test_crear_estudiante(mock_collection):
    mock_insert = MagicMock()
    mock_insert.inserted_id = "est123"
    mock_collection.insert_one = AsyncMock(return_value=mock_insert)
    mock_collection.find_one = AsyncMock(return_value={
        "_id": "est123",
        "nombre": "Juan Pérez",
        "email": "juan@email.com",
        "telefono": "+54 11 1234-5678",
        "fecha_registro": "2024-01-01T00:00:00"
    })

    client = TestClient(app)
    response = client.post("/estudiantes/", json={
        "nombre": "Juan Pérez",
        "email": "juan@email.com",
        "telefono": "+54 11 1234-5678"
    })

    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Juan Pérez"
    assert data["email"] == "juan@email.com"


@patch("app.services.estudiante_service.estudiantes_collection")
def test_listar_estudiantes_vacio(mock_collection):
    mock_collection.find = MagicMock(return_value=AsyncIter([]))

    client = TestClient(app)
    response = client.get("/estudiantes/")
    assert response.status_code == 200
    assert response.json() == []


@patch("app.services.estudiante_service.estudiantes_collection")
def test_obtener_estudiante_no_encontrado(mock_collection):
    mock_collection.find_one = AsyncMock(return_value=None)
    client = TestClient(app)
    response = client.get("/estudiantes/507f1f77bcf86cd799439011")
    assert response.status_code == 404


@patch("app.services.estudiante_service.estudiantes_collection")
def test_eliminar_estudiante_ok(mock_collection):
    mock_collection.delete_one = AsyncMock(return_value=MagicMock(deleted_count=1))
    client = TestClient(app)
    response = client.delete("/estudiantes/507f1f77bcf86cd799439011")
    assert response.status_code == 204
