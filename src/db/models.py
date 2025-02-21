from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
import uuid

class User(SQLModel, table=True):
    id: uuid.UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, nullable=False), 
        default_factory=uuid.uuid4  # Ensure each instance gets a unique UUID
    )
    name: str
    email: str
    password: str

    def __repr__(self):
        return f"<User {self.name}>"
