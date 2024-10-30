from core.models.base_model import BaseModel
from sqlmodel import Field


class User(BaseModel, table=True):
    __tablename__ = "users"

    email: str = Field(unique=True)
    username: str = Field(unique=True)
    first_name: str = Field(default=None, nullable=True)
    last_name: str = Field(default=None, nullable=True)
    password: str = Field()
