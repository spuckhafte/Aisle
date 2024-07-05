from flask_restful import Resource, request

class Signup(Resource):
    def post(self):
        reqData = request.get_json()["payload"]
        username, password = reqData["username"], reqData["password"]

        print(username, password)
        return { "hello": "world" }
