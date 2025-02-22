from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.Authentication.controller.accountController import (
    create_user_controller,
    update_user_controller,
    get_user_controller
)
from src.Authentication.schema.accountSchema import UserCreate, UserRead, UserUpdate
from src.db.database import get_db

router = APIRouter(prefix="/Authentication", tags=["Accounts"])

@router.post("/Account", response_model=UserRead)
async def create_user(data: UserCreate, db: AsyncSession = Depends(get_db)):
    """API endpoint to create a user."""
    return await create_user_controller(data, db)

@router.get("/User/{uid}", response_model=UserRead)
async def get_user(uid: str, db: AsyncSession = Depends(get_db)):  
    """API endpoint to get user by UID."""
    return await get_user_controller(uid, db)

@router.put("/update/{uid}", response_model=UserRead)
async def update_user(uid: str, data: UserUpdate, db: AsyncSession = Depends(get_db)):  
    """API endpoint to update user."""
    return await update_user_controller(uid, data, db) 
