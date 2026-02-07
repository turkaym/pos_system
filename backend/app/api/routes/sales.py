from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user_id
from app.schemas.sale import SaleCreate, SaleOut, SaleListOut
from app.services.sale_service import create_sale
from app.services.sale_read_service import (get_sales, get_sales_by_id)

router = APIRouter(
    prefix="/sales",
    tags=["sales"],
    dependencies=[Depends(get_current_user_id)]
)


@router.post("/", response_model=SaleOut, status_code=status.HTTP_201_CREATED)
def create_sale_endpoint(data: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db=db, data=data)


@router.get("/", response_model=SaleListOut)
def list_sales_endpoint(db: Session = Depends(get_db), limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0),):
    return get_sales(db=db, limit=limit, offset=offset)


@router.get("/{sale_id}", response_model=SaleOut)
def get_sale_endpoint(sale_id: int, db: Session = Depends(get_db)):
    return get_sales_by_id(db=db, sale_id=sale_id)
