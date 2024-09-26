from typing import List
from handlers.custom_mods.ModelDB import Model, Schema, V

class UserSchema(Schema):
    id: V[str]
    birth: V[str]
    username: V[str]
    password: V[str]

    playlists: V[List[int]]
    tracks: V[List[int]]
    friends: V[List[int]]
    recent_plays: V[List[int]]
    
    active_room: V[int]
    current_play: V[int]

    last_login: V[str]

User = Model[UserSchema]
