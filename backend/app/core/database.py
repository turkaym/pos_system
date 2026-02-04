"""
Database configuration and session management.

- Creates SQLAlchemy engine
- Provides DB session dependency
- Central place for DB connection
"""
from app.core import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# ENV VARIABLES
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "pos_db")
DB_USER = os.getenv("DB_USER", "pos_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# DATABASE URL
# mysql+mysqlconnector://user:password@host:port/db_name

DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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
