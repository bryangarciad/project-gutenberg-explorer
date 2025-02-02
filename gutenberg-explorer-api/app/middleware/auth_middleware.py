import re

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.util.http_util import throw_unauthorized_starlet_response
from app.util.jwt import verify_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        headers = request.headers
        auth = headers.get('authorization')

        if not auth: return throw_unauthorized_starlet_response()

        match = re.match(r"^Bearer\s([a-zA-Z0-9-._~+/]+=*)$", auth)
        if not match: return throw_unauthorized_starlet_response()

        token = match.group(1)
        payload = verify_token(token)
        request.state.payload = payload
        response = await call_next(request)
        return response
