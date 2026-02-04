from sqlalchemy import Column, Integer, DECIMAL, String, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(DECIMAL(10, 3), nullable=False, default=0)
    unit = Column(Enum("kg", "unit"), nullable=False)
    is_activa = Column(Boolean, default=True, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    # Relationship
    sale_items = relationship(
        "SaleItem",
        back_populates="product",
        lazy="select",
    )
