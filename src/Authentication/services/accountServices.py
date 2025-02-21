from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from sqlalchemy.future import select
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import uuid


from src.Authentication.models.accountModel import User
from src.Authentication.schema.accountSchema import UserCreate, UserUpdate, UserRead


async def create_account(data: UserCreate, db: AsyncSession):
    """Service function to create a new user."""
    new_user = User(**data.model_dump())
    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=400, detail=f"Database Error: {str(e)}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected Error: {str(e)}")

async def get_account(uid: uuid.UUID, db: AsyncSession) -> User:
    try:
        if not isinstance(uid, uuid.UUID):
            raise ValueError("Invalid UID format")
        
        query = select(User).where(User.uid == uid)
        result = await db.execute(query)
        existing_user = result.scalars().first()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        return existing_user

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
async def update_account(uid: str, data: UserUpdate, db: AsyncSession) -> User:
    try:
        user_uuid = uuid.UUID(uid)  # Ensure UID is valid
        existing_user = await get_account(user_uuid, db)

        # Ensure data is a dictionary
        update_data = data.model_dump(exclude_unset=True)
        if not isinstance(update_data, dict):
            raise ValueError(f"Expected a dictionary, but got: {type(update_data)}")

        if not update_data:
            raise HTTPException(status_code=400, detail="No valid fields provided for update")

        # Apply updates dynamically
        for key, value in update_data.items():
            setattr(existing_user, key, value)

        db.add(existing_user)  # Mark the user as modified
        await db.commit()
        await db.refresh(existing_user)

        return existing_user

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    except HTTPException:
        raise  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
