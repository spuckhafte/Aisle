from typing import cast
from dotenv import dotenv_values

config = dotenv_values(".env")

def getEnv(key: str) -> str:
    env_val = config[key] if config[key] else ""
    return cast(str, env_val)
        
