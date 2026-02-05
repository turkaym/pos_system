from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, data: ProductCreate) -> Product:
    product = Product(
        name=data.name,
        price=data.price,
        stock=data.stock,
        unit=data.unit,
        is_active=data.is_active
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(*, db: Session, product_id: int, data: ProductUpdate) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product
