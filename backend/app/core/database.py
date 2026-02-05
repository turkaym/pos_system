"""
Database configuration and session management.

- Creates SQLAlchemy engine
- Provides DB session dependency
- Central place for DB connection
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core import config
# DATABASE URL
# mysql+mysqlconnector://user:password@host:port/db_name

DATABASE_URL = (
    f"mysql+mysqlconnector://{config.DB_USER}:"
    f"{config.DB_PASSWORD}@"
    f"{config.DB_HOST}:"
    f"{config.DB_PORT}/"
    f"{config.DB_NAME}"
)

# SQLALCHEMY ENGINE
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=1800
)

# SESSION

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# BASE MODEL
Base = declarative_base()

# Dependecy


def get_db():
    """
    FastAPI dependency
    Yields a database session and ensures it is closed
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
