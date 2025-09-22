import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

def test_read_pets_empty(client):
    response = client.get("/pets")
    assert response.status_code == 404


def test_create_pet(client):
    pet_data = {
        "nome": "Nilah",
        "data_nascimento": "2021-12-27",
        "tipo": "Gato",
        "raca": "SRD",
        "cor": "Rajado",
        "castrado": True,
    }

    response = client.post("/pets", json=pet_data)
    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["nome"] == pet_data["nome"]
    assert data["tipo"] == pet_data["tipo"]
    assert data["raca"] == pet_data["raca"]


def test_list_pets(client):
    pet_data = {
        "nome": "Nilah",
        "data_nascimento": "2021-12-27",
        "tipo": "Gato",
        "raca": "SRD",
        "cor": "Rajado",
        "castrado": True,
    }
    response_post = client.post("/pets", json=pet_data)
    created = response_post.json()

    response = client.get("/pets")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert any(p["id"] == created["id"] for p in data)

    pet_returned = next(p for p in data if p["id"] == created["id"])
    assert pet_returned["nome"] == pet_data["nome"]
    assert pet_returned["tipo"] == pet_data["tipo"]


def test_get_pet_by_id(client):
    pet_data = {
        "nome": "Nilah",
        "data_nascimento": "2021-12-27",
        "tipo": "Gato",
        "raca": "SRD",
        "cor": "Rajado",
        "castrado": True,
    }
    response_post = client.post("/pets", json=pet_data)
    created = response_post.json()
    pet_id = created["id"]
    
    response = client.get(f"/pets/{pet_id}")
    assert response.status_code == 200
    data = response.json()
    
    assert data["id"] == pet_id
    assert data["nome"] == pet_data["nome"]
    assert data["tipo"] == pet_data["tipo"]


def test_get_pet_by_name(client):
    pet_data = {
        "nome": "Nilah",
        "data_nascimento": "2021-12-27",
        "tipo": "Gato",
        "raca": "SRD",
        "cor": "Rajado",
        "castrado": True,
    }
    response_post = client.post("/pets", json=pet_data)
    created = response_post.json()
    
    response = client.get(f"/pets?nome={pet_data['nome']}")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) == 1
    pet = data[0]
    
    assert pet["id"] == created["id"]
    assert pet["nome"] == pet_data["nome"]
    assert pet["tipo"] == pet_data["tipo"]


def test_get_nonexistent_pet(client):
    response = client.get("/pets?id=00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
