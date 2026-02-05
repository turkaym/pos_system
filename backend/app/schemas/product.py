from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal
from typing import Literal, Optional
from datetime import datetime


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: Decimal = Field(..., gt=0)
    stock: Decimal = Field(..., gt=0)
    unit: Literal["kg", "unit"]
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    price: Optional[Decimal] = Field(None, gt=0)
    stock: Optional[Decimal] = Field(None, ge=0)
    unit: Optional[Literal["kg", "unit"]] = None
    is_active: Optional[bool] = None


class ProductOut(BaseModel):
    id: int
    name: str
    price: Decimal
    stock: Decimal
    unit: Literal["kg", "unit"]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
