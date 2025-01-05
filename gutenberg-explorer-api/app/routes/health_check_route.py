from fastapi import APIRouter

health_check_router = APIRouter()

@health_check_router.get("/")
async def root():
    return {"message": "OK"}
