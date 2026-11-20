from collections.abc import Generator

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

from app.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker[Session](bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()