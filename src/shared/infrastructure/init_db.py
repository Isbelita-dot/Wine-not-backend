from src.shared.infrastructure.database import Base, engine

from src.category.infrastructure.model import Category
from src.wine.infrastructure.model import Wine
from src.feedback.infrastructure.model import Feedback
"""
Importar modelos para registrar tablas
"""
def init_db() -> None:
    Base.metadata.create_all(bind=engine)