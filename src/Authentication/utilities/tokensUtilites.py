from datetime import datetime, timedelta
from src.config import Config
import jwt
import uuid
import logging



ACCESS_TOKEN_EXPIRY = Config.ACCESS_TOKEN_EXPIRY
JWT_ALGORITHM = Config.JWT_ALGORITHM
JWT_SECRET = Config.JWT_SECRET


def create_tokens(user_data: dict, expireAt: timedelta = None, refresh: bool = False):
    payload = {}

    payload["User"] = user_data
    payload["exp"] = datetime.now() + (expireAt if expireAt is not None else timedelta(hours=ACCESS_TOKEN_EXPIRY))
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM
    )
    return token



def decode_tokens(token: str) -> dict:
    try:
        token_data= jwt.decode(
              jwt==token, key=JWT_SECRET, algorithm=JWT_ALGORITHM
        )
        return token
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None