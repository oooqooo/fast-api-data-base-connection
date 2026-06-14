from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings

# Base class for models
Base = declarative_base()

# SQL Server connection
engine = create_engine(
    settings.db_connection,
    echo=True  # shows SQL queries in terminal (good for learning)
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



        