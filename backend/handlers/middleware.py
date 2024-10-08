from collections.abc import Callable, Iterable
from time import time
from wsgiref.types import StartResponse, WSGIEnvironment
from werkzeug.wrappers import Request, Response
from handlers.funcs import getClientIP, getEnv, keyValid
import json
import jwt

"""
environ.auth_status:
    ~ PASS: proceed with the actual request
    ~ FAIL: unauthorized request, abort the proceeding request
"""

SESSION_EXP_DELTA = 2 * 24 * 60 * 60 # 2 days in seconds

class middleware():
    def __init__(self, app: Callable[[WSGIEnvironment, StartResponse], Iterable[bytes]]):
        self.app = app

    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse):
        # defaults
        environ["auth_status"] = "FAIL"
        request = Request(environ);
        failed_res = Response(
                response=u"auth failed", 
                mimetype= "text/plain", 
                status=401
                )
        reqHeaders = request.headers.get("Authorization")
        if reqHeaders is None or reqHeaders == "":
            return failed_res(environ, start_response)

        authData: dict[str, str] = json.loads(reqHeaders)
        
        print(authData, "auth")
        if not request.environ["REMOTE_ADDR"]:
            return failed_res(environ, start_response)
        
        # for manual login and signup, only ip is required
        if request.path.startswith("/login") or request.path.startswith("/signup"):
            environ["auth_status"] = "PASS"
            return self.app(environ, start_response)
        
        if not keyValid("token", authData):
            return failed_res(environ, start_response)


        token = authData["token"]
        ip = getClientIP(request)
        decoded_jwt = jwt.decode(token, getEnv("ACCESS_TOKEN_SECRET"), algorithms=["HS256"])
        
        print(decoded_jwt, "decode")

        ip_decoded: str = decoded_jwt["ip"]
        birth: int = decoded_jwt["birth"]
        
        # change in ip
        if ip != ip_decoded:
            return failed_res(environ, start_response)

        # session expired
        if time() - birth >= SESSION_EXP_DELTA:
            return failed_res(environ, start_response)
        
        environ["auth_status"] = "PASS"
        return self.app(environ, start_response)

