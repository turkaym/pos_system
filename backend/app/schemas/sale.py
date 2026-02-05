from pydantic import BaseModel, Field, ConfigDict
from typing import List, Literal
from decimal import Decimal
from datetime import datetime


class SaleItemCreate(BaseModel):
    product_id: int
    quantity: Decimal = Field(..., gt=0)


class SaleCreate(BaseModel):
    payment_method: Literal["cash", "card", "transfer"]
    items: List[SaleItemCreate]


class SaleItemOut(BaseModel):
    product_id: int
    quantity: Decimal
    price: Decimal
    subtotal: Decimal

    model_config = ConfigDict(from_attributes=True)


class SaleOut(BaseModel):
    id: int
    total: Decimal
    payment_method: str
    created_at: datetime
    items: List[SaleItemOut]

    model_config = ConfigDict(from_attributes=True)
