from app.models.upsert_user import UpsertUser
from app.models.user import User
from app.helpers.security_password_hash_helper import hash_password
from uuid import uuid4
import datetime

class UserRepository:
    def __init__(self, session,  config: dict):
        self.__config = config
        self.__session = session

    def create_user(self, user: UpsertUser):
        new_user = User(
            id=uuid4(),
            firstName=user.first_name,
            lastName=user.last_name,
            email=user.email,
            passwordHash=hash_password(user.password, self.__config),
            createdAt=datetime.datetime.now()
        )

        new_user.save(self.__session)
