from json import dumps

from app.models.upsert_user import UpsertUser
from app.models.user_credentials import UserCredentials
from app.repositories.user_repository import UserRepository
from app.util.http_util import throw_invalid_credentials, ok, generic_error
from app.util.jwt import get_token
from fastapi import Response, Request, HTTPException, status
from bcrypt import checkpw


class UserController:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def create_user(self, upsert_user: UpsertUser, response: Response):
        try:
            if self.__user_repository.user_exist_by_email(upsert_user.email):
                response.status_code = status.HTTP_409_CONFLICT
                return {"message": "User with this email already exists"}

            self.__user_repository.create_user(upsert_user)
            return ok()
        except Exception as _:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return generic_error()

    async def login_user(self, user_credentials: UserCredentials, response: Response):
        try:
            user = self.__user_repository.get_user_by_email(user_credentials.email)

            if not user: return throw_invalid_credentials()

            if checkpw(user_credentials.password.encode("utf-8"), user.passwordHash.encode("utf-8")):
                return {"token": get_token(
                    payload={"uid": str(user.id), "email": user.email}
                )}

            return throw_invalid_credentials()
        except HTTPException as err:
            return {"message": err.detail}
        except Exception as _:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return generic_error()

    async def get_user_from_jwt(self, request: Request):
        return {"data": dumps(request.state.current)}
