"""
Authentication Business Logic
Clean, focused service layer - no FastAPI dependencies here.
"""

from typing import Dict, Any, Optional, Tuple
from datetime import datetime
import uuid

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..pqc.hybrid import hybrid_auth
from ..utils.jwt import hybrid_jwt
from .models import User, RefreshToken
from .schemas import UserCreate, UserLogin, TokenResponse


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class AuthService:
    """Core authentication logic - pure Python, easy to test."""

    def __init__(self, db: Session):
        self.db = db

    def _hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def _verify_password(self, plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)

    def register(self, user_data: UserCreate) -> Tuple[User, str]:
        """Register new user and return user + initial access token."""
        if self.db.query(User).filter(User.email == user_data.email).first():
            raise ValueError("Email already registered")

        # Generate hybrid keypair for this user (for signing their tokens)
        keys = hybrid_auth.generate_hybrid_keypair()

        user = User(
            id=str(uuid.uuid4()),
            email=user_data.email,
            hashed_password=self._hash_password(user_data.password),
            full_name=user_data.full_name,
            # Store public keys (private keys should be in secure storage in prod)
            classical_public_key=keys["x25519_public"],
            pqc_public_key=keys["dsa_public"],
            # In production: encrypt private keys or use HSM/KMS
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        # Create initial token
        token = self._create_token(user)
        return user, token

    def login(self, credentials: UserLogin) -> Tuple[User, str]:
        """Authenticate user and return new hybrid token."""
        user = self.db.query(User).filter(User.email == credentials.email).first()
        if not user or not self._verify_password(credentials.password, user.hashed_password):
            raise ValueError("Invalid email or password")

        token = self._create_token(user)
        return user, token

    def _create_token(self, user: User) -> str:
        """Create hybrid JWT for a user."""
        claims = {
            "sub": user.id,
            "email": user.email,
            "role": user.role,
        }

        # In production: load private keys from secure vault/HSM
        # For demo/standalone: we can simulate or store temporarily
        return hybrid_jwt.create(
            claims=claims,
            classical_private_key=b"demo-classical-private-key",   # Replace with real key in prod
            pqc_private_key=b"demo-pqc-private-key",               # Replace with real key in prod
        )

    def verify_token(self, token: str) -> Dict[str, Any]:
        """Verify hybrid JWT and return payload."""
        # In production: fetch public keys from user record or cache
        return hybrid_jwt.verify(
            token=token,
            classical_public_key=b"demo-classical-public-key",
            pqc_public_key=b"demo-pqc-public-key",
        )

    def refresh_token(self, old_token: str) -> str:
        """Simple refresh logic (extend in production with refresh token table)."""
        payload = self.verify_token(old_token)
        # In real implementation: check refresh token validity, rotate, etc.
        user = self.db.query(User).filter(User.id == payload["sub"]).first()
        if not user:
            raise ValueError("User not found")
        return self._create_token(user)
