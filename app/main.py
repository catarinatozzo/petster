from fastapi import FastAPI
from app.database import engine, Base
from app.api.routes import pets

Base.metadata.create_all(bind=engine)

api = FastAPI(title="Petster API")

api.include_router(pets.router)