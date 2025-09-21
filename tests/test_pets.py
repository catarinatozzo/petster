from fastapi.testclient import TestClient
from app.main import api

from app.database import get_db
from app.models import Pet

client = TestClient(api)

def test_read_pets_empty():
    db = next(get_db())
    db.query(Pet).delete()  # limpa tabela
    db.commit()

    response = client.get("/pets")
    assert response.status_code == 404
