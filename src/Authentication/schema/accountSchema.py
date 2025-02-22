from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uuid
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    username: EmailStr  
    password: str = Field(min_length=1)
    country_id: Optional[int] = None  
    gender: Optional[str] = None  
    is_system_user: Optional[bool] = None  

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[EmailStr] = None
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
