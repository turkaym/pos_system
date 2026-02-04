from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from typing import Literal
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    price: Decimal
    stock: Decimal
    unit: Literal["kg", "unit"]
    is_active: bool


class ProductOut(BaseModel):
    id: int
    name: str
    price: Decimal
    stock: Decimal
    unit: Literal["kg", "unit"]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class config:

        model_config = ConfigDict(from_attributes=True)
