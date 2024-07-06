from supabase import create_client
from handlers.funcs import getEnv

url = getEnv("SUPA_URL")
key = getEnv("SUPA_KEY")
user_name = getEnv("SUPA_DB_MAIL")
user_pass = getEnv("SUPA_DB_PASS")

class DBClient:
    def __init__(self) -> None:
        self.client = create_client(url, key)
        self.client.auth.sign_in_with_password(
                { 
                 "email": user_name,
                 "password": user_pass,
                 })

        self.Users = self.client.table("Users")

db = DBClient()
