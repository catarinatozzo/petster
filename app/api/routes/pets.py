from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Pet
from app.api.schemas import PetCreate, PetRead
from typing import List, Optional
from app.exceptions.pet_exceptions import PetNotFoundException

router = APIRouter(prefix="/pets", tags=["pets"])

@router.post("/", response_model=PetRead)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = Pet(**pet.model_dump())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.get("/", response_model=List[PetRead])
def read_pets(
    id: str | None = Query(None),
    nome: str | None = Query(None),
    tipo: str | None = Query(None),
    raca: str | None = Query(None),
    cor: str | None = Query(None),
    castrado: bool | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Pet)

    if id:
        query = query.filter(Pet.id == id)
    if nome:
        query = query.filter(Pet.nome.ilike(f"%{nome}%"))
    if tipo:
        query = query.filter(Pet.tipo == tipo)
    if raca:
        query = query.filter(Pet.raca == raca)
    if cor:
        query = query.filter(Pet.cor == cor)
    if castrado is not None:
        query = query.filter(Pet.castrado == castrado)

    results = query.all()
    if not results:
        raise PetNotFoundException(id if id else "with the given filters")
    return results
