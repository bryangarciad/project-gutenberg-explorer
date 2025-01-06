from bcrypt import hashpw

def hash_password(password: str, config: dict) -> str:
    salt = config.get("SALT")
    return hashpw(password, salt)
