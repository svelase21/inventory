import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(
    DATABASE_URL,

    # Try connections before use
    pool_pre_ping=True
)

# Create SessionLocal, a new instance is a new session into database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create declarative base - show model class
Base = declarative_base()

# FastAPI - Dependependencies
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()