from collections.abc import Callable, Iterable
from wsgiref.types import StartResponse, WSGIEnvironment
from werkzeug.wrappers import Request, Response

"""
environ.auth_status:
    ~ PASS: proceed with the actual request
    ~ FAIL: unauthorized request, abort the proceeding request
"""

class middleware():
    def __init__(self, app: Callable[[WSGIEnvironment, StartResponse], Iterable[bytes]]):
        self.app = app
        self.userName = 'Tony'
        self.password = 'IamIronMan'

    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse):
        # defaults
        environ["auth_status"] = "FAIL"
        request = Request(environ);
        failed_res = Response(
            response=u"Auth Failed", 
            mimetype= 'text/plain', 
            status=401
        )
        
        # for manual login and signup, auth is not required
        if request.path.startswith("/login") or request.path.startswith("/signup"):
            environ["auth_status"] = "PASS"
            return self.app(environ, start_response)

        if not request.authorization or not request.authorization.token or not request.authorization.ip:
            return failed_res(environ, start_response)

        # token = request.authorization["token"]
        # ip = request.authorization["ip"]

        # (perform an oldschool auth with token and ip) 
        
        return failed_res(environ, start_response)

