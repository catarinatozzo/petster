from fastapi.testclient import TestClient
from app.main import app 

from app.database import get_db
from app.models import Pet

client = TestClient(app)

def test_read_pets_empty():
    db = next(get_db())
    db.query(Pet).delete()  # limpa tabela
    db.commit()

    response = client.get("/pets")
    assert response.status_code == 404
