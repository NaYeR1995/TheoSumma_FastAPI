from src.db.database import async_engine
from sqlmodel import SQLModel


# 🚨 Import all models before creating tables
from models import User  

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

