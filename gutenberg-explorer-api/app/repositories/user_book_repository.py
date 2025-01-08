import datetime

from app.models.user_books import UserBook

class UserBookRepository:
    def __init__(self, session):
        self.__session = session

    def add_book_to_user_list(self, current_user: dict, book_id: str):
        new_user_book = UserBook(
            userId=current_user.id,
            bookId=book_id,
            createdAt=datetime.datetime.now()
        )

        new_user_book.save(self.__session)

    def get_reading_list(self, current_user: dict):
        reading_list = self.__session.query(UserBook).filter(current_user.userId == current_user.id).all()

        return reading_list
