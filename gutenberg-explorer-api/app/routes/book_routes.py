from fastapi import status
from app.routes.base_router import BaseRouter
from app.controllers.books_controller import BookController
from app.middleware.soft_auth_middleware import SoftAuthMiddleware
class BookRouter(BaseRouter):
    def __init__(self, book_controller: BookController):
        self.book_controller = book_controller
        super().__init__()

    def _setup_routes(self):
        self._router.add_api_route(
            path="/get-book-meta-by-id/{book_id}",
            status_code=status.HTTP_200_OK,
            methods=["GET"],
            endpoint=self.book_controller.get_book_meta
        )

        self._router.add_api_route(
            path="/get-book-text-by-id/{book_id}",
            status_code=status.HTTP_200_OK,
            methods=["GET"],
            endpoint=self.book_controller.get_book_text
        )

        self._sub_app.include_router(self._router)
        self._sub_app.add_middleware(SoftAuthMiddleware)
