from flask_restful import Resource


class LoggedIn(Resource):
    def post(self):
        return "true"
