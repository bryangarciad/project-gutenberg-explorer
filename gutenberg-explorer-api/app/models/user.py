from sqlalchemy import Column, UUID, String, Date
from app.models.base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'User'
    id: Column(UUID, primary_key=True)
    firstName: Column(String)
    lastName: Column(String)
    email: Column(String)
    passwordHash: Column(String)
    createdAt: Column(Date)
