from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)  
    first_name: str = Field(index=True, min_length=1)
    last_name: str = Field(index=True, min_length=1)
    username: str = Field(unique=True, index=True, min_length=1)
    password: str = Field(min_length=1)
    country_id: Optional[int] = Field(default=None, nullable=True)  
    gender: Optional[str] = Field(default=None, nullable=True)  
    is_system_user: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

