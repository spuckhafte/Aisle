from flask import Flask
from flask_restful import Api
from settings import RouteManager
from handlers.middleware import middleware
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__);
api = Api(app);

app.wsgi_app = middleware(app.wsgi_app);

RouteManager(api)

if __name__ == "__main__":
    app.run(debug=True);

