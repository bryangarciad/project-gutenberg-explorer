from sqlalchemy import Column, UUID, String, Date
from sqlalchemy.orm import Mapped
from app.models.base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'User'
    id: Mapped[str] = Column(UUID, primary_key=True)
    firstName: Mapped[str] = Column(String)
    lastName: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    passwordHash: Mapped[str] = Column(String)
    createdAt: Mapped[str] = Column(Date)
