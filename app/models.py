from uuid import uuid4

from sqlalchemy import Column, String, Date, Boolean, Enum as SqlEnum
from sqlalchemy.dialects.mysql import CHAR

from app.database import Base

from app.enums.raca_animal_enum import RacaAnimalEnum
from app.enums.cor_animal_enum import CorAnimalEnum
from app.enums.tipo_animal_enum import TipoAnimalEnum

class Pet(Base):
    __tablename__ = "pets"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    nome = Column(String(50), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    tipo = Column(SqlEnum(TipoAnimalEnum), nullable=False)
    raca = Column(SqlEnum(RacaAnimalEnum), nullable=False)
    cor = Column(SqlEnum(CorAnimalEnum), nullable=False)
    castrado = Column(Boolean, default=False)