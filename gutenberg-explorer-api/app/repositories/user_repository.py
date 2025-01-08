from uuid import uuid4
import datetime

from app.models.upsert_user import UpsertUser
from app.models.user import User
from app.helpers.security_password_hash_helper import hash_password

class UserRepository:
    def __init__(self, session):
        self.__session = session

    def create_user(self, user: UpsertUser):
        password_hashed = hash_password(user.password)
        new_user = User(
            id=uuid4(),
            firstName=user.first_name,
            lastName=user.last_name,
            email=user.email,
            passwordHash=password_hashed,
            createdAt=datetime.datetime.now()
        )

        new_user.save(self.__session)

    def user_exist_by_email(self, email:str) -> bool:
        users = self.__session.query(User).filter(User.email == email).all()

        return len(users) != 0

    def get_user_by_email(self, email:str):
        return self.__session.query(User).filter(User.email == email).first()
