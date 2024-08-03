from flask_restful import Api
from handlers.routes.logged_in import LoggedIn
from handlers.routes.login import Login
from handlers.routes.signup import Signup

resources = {
    "/signup": Signup,
    "/login": Login,
    "/is_logged_in": LoggedIn
}

class RouteManager:
    def __init__(self, api: Api):
        self.api = api
        
        for route in resources:
            self.api.add_resource(resources[route], route)

