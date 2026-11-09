from collections.abc import Generator

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

from app.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)
Sessionlocal = sessionmaker[Session](bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()