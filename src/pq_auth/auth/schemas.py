"""
Pydantic Schemas
Request / Response models - clean and validation-focused.
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    """Request body for user registration."""
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    """Request body for login."""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Safe user data returned to clients."""
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    role: str
    created_at: datetime

    class Config:
        from_attributes = True  # For SQLAlchemy compatibility


class TokenResponse(BaseModel):
    """Response after successful login/register/refresh."""
    access_token: str
    token_type: str = "bearer"
    user: Optional[UserResponse] = None
    expires_in: int = 3600


class TokenVerifyResponse(BaseModel):
    """Response when verifying a token."""
    valid: bool
    payload: dict
    user_id: Optional[str] = None
