from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from contextlib import asynccontextmanager
from src.db.database import get_db
from src.db.models import User
from src.db.create_db import init_db

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


@app.post("/users/")
async def create_user(name: str, email: str, password: str, db: AsyncSession = Depends(get_db)):
    new_user = User(name=name, email=email, password=password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users
