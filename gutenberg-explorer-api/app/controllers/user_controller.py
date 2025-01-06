from app.models.upsert_user import UpsertUser
from app.repositories.user_repository import UserRepository
from fastapi import Response, status

class UserController:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def create_user(self, upsert_user: UpsertUser):
            self.__user_repository.create_user(upsert_user)
