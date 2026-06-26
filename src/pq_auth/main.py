"""
FastAPI Entry Point
Main application - clean and minimal.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .config import get_settings
from .auth.router import router as auth_router
from .auth.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = get_settings()

# Database setup (SQLite for easy local development)
engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables on startup (demo only - use Alembic in production)
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Hybrid Post-Quantum Authentication Service - ML-KEM + ML-DSA",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    """Health check + welcome."""
    return {
        "message": "PQ Auth Service is running",
        "status": "quantum-safe",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    """Simple health check."""
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run("src.pq_auth.main:app", host="0.0.0.0", port=8000, reload=True)
