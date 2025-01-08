from bcrypt import hashpw, gensalt

def hash_password(password: str) -> str:
    salt_bytes  = gensalt()
    password_bytes = password.encode('utf-8')

    return hashpw(password_bytes, salt_bytes).decode("utf-8")
