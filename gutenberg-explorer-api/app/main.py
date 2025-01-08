from os import environ

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.err_handling_middleware import ErrHandlingMiddleware

from app.routes.health_check_route import HealthCheckRoute
from app.routes.public_routes import PublicRouter
from app.routes.user_routes import UserRouter
from app.routes.book_routes import BookRouter
from app.repositories.user_repository import UserRepository
from app.repositories.user_book_repository import UserBookRepository
from app.controllers.user_controller import UserController
from app.controllers.books_controller import BookController
from app.util.db_session_provider import DatabaseSessionProvider

load_dotenv()

app = FastAPI()

config = dict(environ)


database_session_provider = DatabaseSessionProvider(config)
session = database_session_provider.get_session()

user_repository = UserRepository(session=session)
user_book_repository=UserBookRepository(session=session)
user_controller = UserController(user_repository=user_repository)
book_controller = BookController(user_book_repository=UserBookRepository)

public_router = PublicRouter(user_controller=user_controller)
user_router = UserRouter(user_controller=user_controller)
book_router = BookRouter(book_controller=book_controller)
health_check_router = HealthCheckRoute()

app.add_middleware(ErrHandlingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.mount(path="/public", app=public_router.get_sub_application())
app.mount(path="/user", app=user_router.get_sub_application())
app.mount(path="/books", app=book_router.get_sub_application())
app.mount(path="/", app=health_check_router.get_sub_application())

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
