from sqlalchemy import Column, UUID, Date, String
from sqlalchemy.orm import Mapped
from app.models.base_model import BaseModel

class Book(BaseModel):
    __tablename__ = 'Book'
    id:  Mapped[str] = Column(UUID, primary_key=True)
    gutenbergId: Mapped[str] = Column(String)
    coverUrl: Mapped[str] = Column(String)
    author: Mapped[str] = Column(String)
    original_publication: Mapped[str] = Column(String)
    credits: Mapped[str] = Column(String)
    language: Mapped[str] = Column(String)
    category: Mapped[str] = Column(String)
    release_date: Mapped[str] = Column(Date)
    copyright_status: Mapped[str] = Column(String)
    content: Mapped[str] = Column(String)
    createdAt: Mapped[str] = Column(Date)
