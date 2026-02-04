from sqlalchemy import Column, Integer, DECIMAL, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(Enum("cash", "card", "transfer"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship(
        "SaleItem",
        back_populates="sale",
        cascade="all, delete-orphan",
        lazy="select",
    )
