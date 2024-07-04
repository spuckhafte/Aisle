from flask import Flask
from flask_restful import Api, Resource
from handlers.middleware import middleware
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__);
api = Api(app);

app.wsgi_app = middleware(app.wsgi_app);

class Home(Resource):
    def get(self):
        return {
            "data": "hello"
        };

api.add_resource(Home, "/");

if __name__ == "__main__":
    app.run(debug=True);

