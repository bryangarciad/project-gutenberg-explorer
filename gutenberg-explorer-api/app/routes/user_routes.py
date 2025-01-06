from fastapi import APIRouter, status
from app.models.upsert_user import UpsertUser

user_router = APIRouter()

@user_router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(upsert_user: UpsertUser):
    print(upsert_user)
    return {"message": "OK"}
