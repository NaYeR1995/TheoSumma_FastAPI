from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from contextlib import asynccontextmanager
from src.db.database import get_db
from src.db.create_db import init_db

# Routers
from src.Authentication.routes.accountRouter import router as account_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print("🚀 Server Is Starting .....")
    await init_db()
    yield
    print("🛑 Server Has Been Stopped .....")
    
app = FastAPI(
    title="TheoSumma User APIS",
    description="A REST API For USER Web Service .... ",
    lifespan=life_span
)



@app.get("/")
async def home():
    return {"message": "FastAPI & PostgreSQL with Docker"}


# Registering routes
app.include_router(account_router)
