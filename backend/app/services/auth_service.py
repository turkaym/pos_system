from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.core.jwt import create_access_token
from app.core.security import verify_password


def authenticate_user(*, db: Session, username: str, password: str) -> str:
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User inactive")

    return create_access_token({"sub": str(user.id)})
