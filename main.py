from contextlib import asynccontextmanager

from fastapi import FastAPI

from shared.infrastructure.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Wine Not",
    description="Rest API para el e-commerce Wine Not. ",
    version="1.0.0",
    lifespan=lifespan,
)

@app.get("/")
def root():
    return{
        "message": "Bienvenido a la API de Wine Not!"
    }