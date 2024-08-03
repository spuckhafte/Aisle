from flask_restful import Resource, request
from handlers.funcs import getClientIP, getEnv
from handlers.db import db
from handlers.cs import U
from hashlib import sha256
from time import time
import jwt

class Login(Resource):
    def post(self):
        reqHeaders = request.headers.get("Authorization")
        if reqHeaders is None or reqHeaders == "":
            return { 'err': 'auth headers missing' }, 401

        reqDataRaw = request.get_json()
        if not reqDataRaw or not reqDataRaw["payload"]:
            return { 'err': 'no valid payload provided' }, 400
 
        # valid: already questioned in middleware
        payload: dict[str, str] = reqDataRaw["payload"]
 
        if not payload["username"] or not payload["password"]:
            return { 'err': 'no valid payload provided' }, 400
        
        username, password = payload["username"], payload["password"]
        password_hash = sha256(str.encode(password)).hexdigest()
        
        existing_user = [] # len: 0 | 1
        try:
            existing_user = db.Users.select(
                    U().gk(id=True)
                    ).eq("username", username).eq(
                            "password", password_hash
                            ).execute().data
        except Exception as e:
            print(e)
            return { "err": "database failed" }, 500

        if len(existing_user) == 0:
            return { "err": "(showcase)Username or password doesn't exist" }, 400

        encode_data = {
                "ip": getClientIP(request),
                "birth": time()
                }
        encoded_jwt = jwt.encode(encode_data, getEnv("ACCESS_TOKEN_SECRET"))
        
        return {
                "token": encoded_jwt,
                "err": ""
                }       
        
