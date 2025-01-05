from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from app import app

class Application:
    '''
    Application class to handle all required initialization steps; 
    including middleware, and routes registration
    '''
    def __init__(self, middleware: list[BaseHTTPMiddleware], routes: list[APIRouter]):
        self.__middleware = middleware
        self.__routes = routes

        self.__register_cors_middleware()
        self.__register_middleware()
        self.__register_routes()

    def __register_cors_middleware(self):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __register_middleware(self):
        for middleware in self.__middleware:
            app.add_middleware(middleware)

    def __register_routes(self):
        for route in self.__routes:
            app.include_router(route)
