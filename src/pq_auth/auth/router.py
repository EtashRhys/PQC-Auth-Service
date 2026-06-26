"""
FastAPI Router for Authentication Endpoints
Clean, focused, and well-documented.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..config import get_db
from .schemas import UserCreate, UserLogin, TokenResponse, UserResponse
from .service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user and receive hybrid PQC JWT."""
    service = AuthService(db)
    try:
        user, token = service.register(user_data)
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            user=UserResponse.from_orm(user)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/login", response_model=TokenResponse)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """Login and receive hybrid PQC JWT."""
    service = AuthService(db)
    try:
        user, token = service.login(credentials)
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            user=UserResponse.from_orm(user)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(token: str, db: Session = Depends(get_db)):
    """Refresh access token using hybrid verification."""
    service = AuthService(db)
    try:
        new_token = service.refresh_token(token)
        # For simplicity we return minimal user info on refresh
        return TokenResponse(access_token=new_token, token_type="bearer")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


@router.get("/me")
def get_current_user(token: str):
    """Verify token and return user info (demo endpoint)."""
    service = AuthService(None)  # In real use, inject proper DB if needed
    payload = service.verify_token(token)
    return {"user_id": payload.get("sub"), "email": payload.get("email")}
