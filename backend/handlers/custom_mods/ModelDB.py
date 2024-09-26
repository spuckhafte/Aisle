from typing import NotRequired, TypedDict, cast

"""
Example Schema -

class User(Schema):
    id: str,
    name: str,
    addr: Opt[str]
"""

class Model[K]:
    schema: K

    def __init__(self, schema: K):
        self.schema = schema

    def gd(self) -> dict:
        return cast(dict, self.schema)

    def gk(self) -> str:
        key_string = ""

        for key in cast(dict, self.schema).keys():
            key_string += (key + ", ")
        
        return key_string[:len(key_string) - 2]

# each value will be marked as NotRequired
V = NotRequired
Schema = TypedDict

