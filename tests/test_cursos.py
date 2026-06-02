import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from fastapi.testclient import TestClient

from app.main import app


class AsyncIter:
    def __init__(self, items):
        self.items = list(items)

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self.items:
            raise StopAsyncIteration
        return self.items.pop(0)


@patch("app.services.curso_service.cursos_collection")
def test_crear_curso(mock_collection):
    mock_collection.insert_one = AsyncMock(return_value=MagicMock(inserted_id="abc123"))
    mock_collection.find_one = AsyncMock(return_value={
        "_id": "abc123",
        "titulo": "Curso Test",
        "categoria": "Programación",
        "instructor": "Profe",
        "duracion_horas": 10,
        "activo": True
    })

    client = TestClient(app)
    response = client.post("/cursos/", json={
        "titulo": "Curso Test",
        "categoria": "Programación",
        "instructor": "Profe",
        "duracion_horas": 10
    })

    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Curso Test"
    assert data["categoria"] == "Programación"


@patch("app.services.curso_service.cursos_collection")
def test_listar_cursos_vacio(mock_collection):
    mock_collection.find = MagicMock(return_value=AsyncIter([]))

    client = TestClient(app)
    response = client.get("/cursos/")
    assert response.status_code == 200
    assert response.json() == []


@patch("app.services.curso_service.cursos_collection")
def test_listar_cursos_con_datos(mock_collection):
    mock_collection.find = MagicMock(return_value=AsyncIter([
        {
            "_id": "abc123",
            "titulo": "Curso A",
            "categoria": "Programación",
            "instructor": "Profe A",
            "duracion_horas": 10,
            "activo": True
        },
        {
            "_id": "def456",
            "titulo": "Curso B",
            "categoria": "Diseño",
            "instructor": "Profe B",
            "duracion_horas": 20,
            "activo": False
        }
    ]))

    client = TestClient(app)
    response = client.get("/cursos/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["titulo"] == "Curso A"
    assert data[1]["titulo"] == "Curso B"


@patch("app.services.curso_service.cursos_collection")
def test_obtener_curso_no_encontrado(mock_collection):
    mock_collection.find_one = AsyncMock(return_value=None)
    client = TestClient(app)
    response = client.get("/cursos/507f1f77bcf86cd799439011")
    assert response.status_code == 404


@patch("app.services.curso_service.cursos_collection")
def test_obtener_curso_id_invalido(mock_collection):
    client = TestClient(app)
    response = client.get("/cursos/123")
    assert response.status_code == 400


@patch("app.services.curso_service.cursos_collection")
def test_eliminar_curso_no_encontrado(mock_collection):
    mock_collection.delete_one = AsyncMock(return_value=MagicMock(deleted_count=0))
    client = TestClient(app)
    response = client.delete("/cursos/507f1f77bcf86cd799439011")
    assert response.status_code == 404


@patch("app.services.curso_service.cursos_collection")
def test_eliminar_curso_ok(mock_collection):
    mock_collection.delete_one = AsyncMock(return_value=MagicMock(deleted_count=1))
    client = TestClient(app)
    response = client.delete("/cursos/507f1f77bcf86cd799439011")
    assert response.status_code == 204
