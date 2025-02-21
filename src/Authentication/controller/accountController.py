from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
import uuid

from src.Authentication.services.accountServices import create_account, get_account, update_account
from src.Authentication.schema.accountSchema import UserCreate, UserUpdate, UserRead
from src.db.database import get_db


async def create_user_controller(data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_account(data, db)


async def get_user_controller(uid: str, db: AsyncSession = Depends(get_db)):
    return await get_account(uid, db)


async def update_user_controller(uid: str, data: UserUpdate, db: AsyncSession = Depends(get_db)):
    return await update_account(uid, data, db)
