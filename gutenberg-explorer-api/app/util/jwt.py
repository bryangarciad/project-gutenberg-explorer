from datetime import datetime, timedelta
from os import environ
from app.util.http_util import throw_unauthorized_starlet_response
import jwt

def get_token(payload):
    token_payload = {
        **payload,
        'exp': datetime.now() + timedelta(hours=10) 
    }
    token = jwt.encode(token_payload, environ.get("SECRET_KEY"), algorithm='HS256')
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, environ.get("SECRET_KEY"), algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return throw_unauthorized_starlet_response()
    except jwt.InvalidTokenError:
        return throw_unauthorized_starlet_response()
