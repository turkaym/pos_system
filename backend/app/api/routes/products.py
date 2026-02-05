from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.product import Product
from app.schemas.product import ProductOut, ProductCreate, ProductUpdate
from app.services.product_service import update_product as update_product_service
from app.services.product_service import create_product as create_product_servies

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("/", response_model=list[ProductOut])
def get_products_endpoint(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


@router.get("/{product_id}", response_model=ProductOut)
def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    return product


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(data: ProductCreate, db: Session = Depends(get_db)):
    return create_product_servies(db, data)


@router.put("/{product_id}", response_model=ProductOut)
def update_product_endpoint(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return update_product_service(db=db, product_id=product_id, data=data)
