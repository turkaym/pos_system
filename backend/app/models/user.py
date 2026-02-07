from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)
