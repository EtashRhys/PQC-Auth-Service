"""
Configuration Settings
Clean and simple configuration for the entire service.
"""

from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    """Main settings for PQ Auth Service."""
    
    # Application
    APP_NAME: str = "PQ Auth Service"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "sqlite:///./pq_auth.db"
    
    # Security
    JWT_LEEWAY_SECONDS: int = 60
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # PQC Settings
    DEFAULT_KEM_ALG: str = "ML-KEM-768"
    DEFAULT_DSA_ALG: str = "ML-DSA-65"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """Cached settings (best practice)."""
    return Settings()


def get_db_url() -> str:
    """Helper for database URL."""
    return get_settings().DATABASE_URL
