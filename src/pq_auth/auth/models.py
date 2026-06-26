"""
SQLAlchemy Models
Simple, clean database models for the PQ Auth Service.
"""

from sqlalchemy import Column, String, DateTime, Boolean, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()


class User(Base):
    """Main user model with hybrid PQC public keys."""
    
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(String, default="user")
    
    # Hybrid PQC public keys (private keys should be stored in KMS/HSM in production)
    classical_public_key = Column(Text, nullable=True)   # e.g. Ed25519
    pqc_public_key = Column(Text, nullable=True)         # ML-DSA public key
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}>"


class RefreshToken(Base):
    """Optional refresh token storage for production use."""
    
    __tablename__ = "refresh_tokens"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, index=True)
    token_hash = Column(String, nullable=False, unique=True)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_revoked = Column(Boolean, default=False)
