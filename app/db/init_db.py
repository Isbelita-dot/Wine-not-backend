from app.db.base import Base
from app.db.session import engine

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

"""
Creates all database tables if they do not already exist
"""