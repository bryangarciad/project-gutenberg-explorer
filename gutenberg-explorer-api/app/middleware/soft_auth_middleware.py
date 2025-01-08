import re

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.util.jwt import verify_token

class SoftAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        headers = request.headers
        auth = headers.get('authorization')

        if not auth:
            response = await call_next(request)
            return response

        match = re.match(r"^Bearer\s([a-zA-Z0-9-._~+/]+=*)$", auth)
        if not match:
            response = await call_next(request)
            return response

        token = match.group(1)
        payload = verify_token(token)
        request.state.current = payload
        response = await call_next(request)
        return response
