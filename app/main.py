from fastapi import FastAPI
from app.database import engine, Base
from app.api.routes import pets

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Petster API")

app.include_router(pets.router)