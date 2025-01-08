from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class ErrHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as _:
            return {"message": "something went wrong"}
