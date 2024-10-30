from typing import Optional

from core.models.base_model import BaseModel
from sqlmodel import Field


class Character(BaseModel, table=True):
    __tablename__ = "characters"

    name: str = Field(unique=True, nullable=False)
    height: float = Field(nullable=False)
    mass: float = Field(nullable=False)
    hair_color: str = Field(nullable=False)
    skin_color: str = Field(nullable=False)
    eye_color: str = Field(nullable=False)

    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
