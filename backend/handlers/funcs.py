from typing import cast
from dotenv import dotenv_values
from werkzeug.wrappers import Request

config = dotenv_values(".env")

def getEnv(key: str) -> str:
    env_val = config[key] if config[key] else ""
    return cast(str, env_val)

def keyValid(key: str, dic: dict[str, str]):
    keyIsValid = not dic or key not in dic.keys() or not dic[key]
    return False if keyIsValid else True

def getClientIP(request: Request):
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

