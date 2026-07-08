from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.shared.infrastructure.init_db import init_db

from src.wine.infrastructure.api import router as wine_router
#from src.category.infrastructure.api import router as category_router
#from src.feedback.infrastructure.api import router as feedback_router

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

app.include_router(wine_router)
#app.include_router(category_router)
#app.include_router(feedback_router)