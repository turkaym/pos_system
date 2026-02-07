from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.sale import Sale


def get_sales(*, db: Session, limit: int = 20, offset: int = 0):
    query = db.query(Sale).order_by(Sale.created_at.desc())

    total = query.count()
    sales = query.offset(offset).limit(limit).all()

    return {
        "total": total,
        "items": sales,
    }


def get_sales_by_id(*, sale_id: int, db: Session) -> Sale:
    sale = (
        db.query(Sale).filter(Sale.id == sale_id).first()
    )

    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")

    return sale
