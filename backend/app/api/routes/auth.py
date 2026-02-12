from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.core.database import get_db
from app.services.auth_service import authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    token = authenticate_user(
        db=db,
        username=form_data.username,
        password=form_data.password,
    )
    return {
        "access_token": token,
        "token_type": "bearer",
    }
