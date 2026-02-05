from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.sale import SaleCreate, SaleOut
from app.services.sale_service import create_sale

router = APIRouter(
    prefix="/sales",
    tags=["sales"]
)


@router.post("/", response_model=SaleOut, status_code=status.HTTP_201_CREATED)
def create_sale_endpoint(data: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db=db, data=data)
