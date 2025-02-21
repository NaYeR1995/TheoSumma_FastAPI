from sqlmodel import SQLModel
from src.db.database import async_engine


# Import all models before creating tables
from src.Authentication.models.accountModel import User

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)  # ✅ Creates all tables
