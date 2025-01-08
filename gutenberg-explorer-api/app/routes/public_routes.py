from fastapi import status
from app.controllers.user_controller import UserController
from app.routes.base_router import BaseRouter

class PublicRouter(BaseRouter):
    def __init__(self, user_controller: UserController):
        self.__user_controller = user_controller
        super().__init__()

    def _setup_routes(self):
        self._router.add_api_route(
            path="/create-user",
            status_code=status.HTTP_201_CREATED,
            methods=["POST"],
            endpoint=self.__user_controller.create_user
        )

        self._router.add_api_route(
            path="/authenticate",
            status_code=status.HTTP_200_OK,
            methods=["POST"],
            endpoint=self.__user_controller.login_user
        )

        self._sub_app.include_router(self._router)
