# from pydantic import BaseModel

# structure of model

# class User(BaseModel):

#     name: str
#     email: str
#     password: str

from pydantic import BaseModel

class User(BaseModel):
    # id: int  # Manually typed integer ID
    name: str
    email: str
    mobile_number:int
    location:str
    password: str


    




