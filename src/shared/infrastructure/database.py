from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.shared.infrastructure.config import settings

from src.category.infrastructure.model import Category
from src.wine.infrastructure.model import Wine
from src.feedback.infrastructure.model import Feedback

#Conexión base de datos
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#Fábrica de sesiones
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#Clase base para los modelos
Base = declarative_base()

__all__ = [
    "Base",
    "SessionLocal",
    "engine",
    "Category",
    "Wine",
    "Feedback"
]