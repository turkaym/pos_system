from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from decimal import Decimal
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.schemas.sale import SaleCreate


def create_sale(*, db: Session, data: SaleCreate) -> Sale:
    if not data.items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Sale must contain at least one item")

    total = Decimal("0.00")

    with db.begin():
        sale = Sale(
            total=Decimal("0.00"),
            payment_method=data.payment_method
        )

        db.add(sale)
        db.flush()

        for item in data.items:
            product = (
                db.query(Product).filter(Product.id ==
                                         item.product_id).with_for_update().first()
            )

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Product {item.product_id} not found")

        if not product.is_active:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Product {item.product_id} is inactive")

        if product.stock < item.quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Insufficient stock for product {product.name}")

        product.stock -= item.quantity

        subtotal = item.quantity * product.price
        total += subtotal

        sale_item = SaleItem(
            sale_id=sale.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price,
            subtotal=subtotal
        )

        db.add(sale_item)

    sale.total = total

    return sale
