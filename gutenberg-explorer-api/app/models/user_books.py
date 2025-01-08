from sqlalchemy import Column, UUID, Boolean, Date
from sqlalchemy.orm import Mapped
from app.models.base_model import BaseModel

class UserBook(BaseModel):
    __tablename__ = 'UserBooks'
    userId: Mapped[str] = Column(UUID)
    bookId: Mapped[str] = Column(UUID, primary_key=True)
    readLater: Mapped[bool] = Column(Boolean)
    downloaded: Mapped[bool] = Column(Boolean)
    createdAt:  Mapped[str] = Column(Date)
