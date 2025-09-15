from uuid import UUID
from datetime import date

from pydantic import BaseModel

from app.enums.raca_animal_enum import RacaAnimalEnum
from app.enums.cor_animal_enum import CorAnimalEnum
from app.enums.tipo_animal_enum import TipoAnimalEnum

class PetBase(BaseModel):
    nome: str
    data_nascimento: date
    tipo: TipoAnimalEnum
    raca: RacaAnimalEnum
    cor: CorAnimalEnum
    castrado: bool = False

class PetCreate(PetBase):
    pass

class PetRead(PetBase):
    id: UUID

    class Config:
        orm_mode = True
