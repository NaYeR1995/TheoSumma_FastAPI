from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: EmailStr  
    password: str  
    country_id: Optional[int] = None
    gender: Optional[str] = None
    is_system_user: Optional[bool] = None

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    country_id: Optional[int] = None
    gender: Optional[str] = None
    is_system_user: Optional[bool] = None

class UserRead(BaseModel):
    uid: uuid.UUID
    first_name: str
    last_name: str
    username: str
    country_id: Optional[int] = None
    gender: Optional[str] = None
    is_system_user: bool
    created_at: datetime
    updated_at: datetime
