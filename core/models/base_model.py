from datetime import datetime

from sqlmodel import Field, func, SQLModel


class BaseModel(SQLModel):
    id: int = Field(default=None, primary_key=True, index=True, nullable=False)
    created_at: datetime = Field(default=func.now())
    updated_at: datetime = Field(default=func.now())
