from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@localhost:5432/auth_db"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
