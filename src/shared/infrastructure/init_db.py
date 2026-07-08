from src.shared.infrastructure.database import Base, engine

"""
Creates all database tables if they do not already exist
"""
def init_db() -> None:
    Base.metadata.create_all(bind=engine)