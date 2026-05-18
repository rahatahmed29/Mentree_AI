# Creates the SQLAlchemy engine and session factory.
# Every route gets a DB session through FastAPI dependency injection.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency (very important for FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()