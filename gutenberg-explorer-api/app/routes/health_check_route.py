from fastapi import APIRouter, status

health_check_router = APIRouter()

@health_check_router.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "OK"}
