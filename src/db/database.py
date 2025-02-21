from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.config import Config

DATABASE_URL = Config.DATABASE_URL

# Create an async engine (Manages DB connection)
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory (Creates independent DB sessions per request)
AsyncSessionLocal = sessionmaker(
    bind=async_engine,  # Connects the session to the database
    class_=AsyncSession,  # Uses async sessions instead of sync
    expire_on_commit=False  # Keeps objects in memory after commit
)

# Dependency function to provide a database session for each request
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session  # Opens a session for the request, then automatically closes it
