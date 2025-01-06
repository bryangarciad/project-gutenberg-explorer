from os import environ

from app import app # pylint: disable=unused-import
from app.application.application import Application

from app.middleware.auth_middleware import AuthMiddleware

from app.routes.health_check_route import health_check_router
from app.routes.user_routes import user_router

from app.util.db_session_provider import DatabaseSessionProvider

config = dict(environ)

database_session_provider = DatabaseSessionProvider(config)
session = database_session_provider.get_session()

middleware = [AuthMiddleware]
routes = [health_check_router, user_router]

Application(
    middleware=middleware,
    routes=routes
)
