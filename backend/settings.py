from flask_restful import Api
from handlers.routes.signup import Signup

resources = {
    "/signup": Signup,
}

class RouteManager:
    def __init__(self, api: Api):
        self.api = api
        
        for route in resources:
            self.api.add_resource(resources[route], route)

