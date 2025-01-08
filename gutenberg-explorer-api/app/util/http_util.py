from fastapi import HTTPException
from starlette.responses import JSONResponse

def throw_unauthorized():
    raise HTTPException(status_code=401, detail="Unauthorized")

def throw_unauthorized_starlet_response():
    return JSONResponse(content={"message": "Unauthorized"}, status_code=401)

def throw_invalid_credentials():
    raise HTTPException(status_code=401, detail="Invalid Credentials")

def ok():
    return {"message": "OK"}

def generic_error():
    return {"message": "Something went wrong"}

def throw_book_not_found():
    raise HTTPException(status_code=404, detail="book not found or does not exists")
