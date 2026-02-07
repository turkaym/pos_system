from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token = authenticate_user(
        db=db,
        username=data.username,
        password=data.password
    )

    return {"access_token": token}
