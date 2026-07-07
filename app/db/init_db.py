from app.db.base import Base
from app.db.session import engine

"""
Creates all database tables if they do not already exist
"""
def init_db() -> None:
    Base.metadata.create_all(bind=engine)