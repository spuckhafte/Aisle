import json
from time import time
from flask_restful import Resource, request
from hashlib import sha256
from handlers.cs import U
from handlers.funcs import getEnv
import jwt
from handlers.db import db

EXPIRE_DELTA_DAY = 2

ACCESS_TOKEN_SECRET = getEnv("ACCESS_TOKEN_SECRET")
REFRESH_TOKEN_SECRET = getEnv("REFRESH_TOKEN_SECRET")

class Signup(Resource):
    def post(self):
        reqHeaders = request.headers.get("Authorization")
        if reqHeaders is None or reqHeaders == "":
            return { 'err': 'auth headers missing' }, 401

        reqDataRaw = request.get_json()
        if not reqDataRaw or not reqDataRaw["payload"]:
            return { 'err': 'no valid payload provided' }, 400
    
        authData: dict[str, str] = json.loads(reqHeaders)
        payload: dict[str, str] = reqDataRaw["payload"]
 
        username, password = payload["username"], payload["password"]
        password_hash = sha256(str.encode(password)).hexdigest()

        user_with_similar_name = db.Users.select(U().gk(username=True)).eq("username", username).execute()
        if len(user_with_similar_name.data) > 0:
            return { "err": "username already exists" }, 400

        encode_data = {
                "ip": authData["ip"],
                "birth": time()
                }
        encoded_jwt = jwt.encode(encode_data, ACCESS_TOKEN_SECRET, algorithm="HSA256")

        return { 
                "token": encoded_jwt,
                "err": "",
                }

    def get(self):
        return { "hello": "world" }
