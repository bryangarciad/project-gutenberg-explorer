from fastapi import status
from app.routes.base_router import BaseRouter
from app.controllers.user_controller import UserController
from app.middleware.auth_middleware import AuthMiddleware

class UserRouter(BaseRouter):
    def __init__(self, user_controller: UserController):
        self.__user_controller = user_controller
        super().__init__()

    def _setup_routes(self):
        self._router.add_api_route(
            path="/get-current-user-info",
            status_code=status.HTTP_200_OK,
            methods=["GET"],
            endpoint=self.__user_controller.get_user_from_jwt
        )

        self._sub_app.include_router(self._router)
        self._sub_app.add_middleware(AuthMiddleware)
