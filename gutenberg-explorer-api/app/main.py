from app import app

from app.application.application import Application
from app.middleware.auth_middleware import AuthMiddleware

from app.routes.health_check_route import health_check_router

middleware = [AuthMiddleware]
routes = [health_check_router]

Application(
    middleware=middleware,
    routes=routes
)
