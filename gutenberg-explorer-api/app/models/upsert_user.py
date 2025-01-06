from pydantic import BaseModel

class UpsertUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
