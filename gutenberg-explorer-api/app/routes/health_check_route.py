from fastapi import status
from app.routes.base_router import BaseRouter

class HealthCheckRoute(BaseRouter):
    def _setup_routes(self):
        self._router.add_api_route(
            path="/",
            status_code=status.HTTP_200_OK,
            methods=["GET"],
            endpoint=lambda : {"message": "OK"}
        )

        self._sub_app.include_router(self._router)
