

# from fastapi import APIRouter, HTTPException
# from models.user import User
# from config.db import conn
# from schemas.user import userEntity, usersEntity

# user = APIRouter(prefix="/api/v1/user")

# @user.get('/')
# async def find_all_users():
#     users = list(conn.local.user.find())
#     return usersEntity(users)

# @user.post('/')
# async def create_user(user: User):
#     user_dict = dict(user)
#     conn.local.user.insert_one(user_dict)
#     return userEntity(user_dict)

# @user.put('/{id}')
# async def update_user(id: int, user: User):
#     user_dict = dict(user)
#     result = conn.local.user.update_one(
#         {"id": id},
#         {"$set": user_dict}
#     )

#     if result.modified_count == 1:
#         return userEntity(user_dict)
#     else:
#         raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    
# @user.get('/{id}')
# async def get_user(id: int):
#     user = conn.local.user.find_one({"id": id})
#     if user:
#         return userEntity(user)
#     else:
#         raise HTTPException(status_code=404, detail=f"User with id {id} not found")

# @user.delete('/{id}')
# async def delete_user(id: int):
#     result = conn.local.user.delete_one({"id": id})

#     if result.deleted_count == 1:
#         return {"message": f"User with id {id} deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail=f"User with id {id} not found")

from fastapi import APIRouter, HTTPException
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bcrypt import hashpw, gensalt

user = APIRouter(prefix="/api/v1/user",tags=['User'])

def get_next_sequence_value(sequence_name):
    seq = conn.local.counters.find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"sequence_value": 1}},
        upsert=True,
        return_document=True
    )

    return seq["sequence_value"]

@user.get('/')
async def find_all_users():
    users = list(conn.local.user.find())
    return usersEntity(users)

@user.post('/')
async def create_user(user: User):
    user_dict = user.dict()
    user_dict['id'] = get_next_sequence_value('userid')  # Assign sequential ID
    user_dict['password'] = hashpw(user.password.encode('utf-8'), gensalt()).decode('utf-8')
    conn.local.user.insert_one(user_dict)
    return userEntity(user_dict)

@user.put('/{id}')
async def update_user(id: int, user: User):
    user_dict = user.dict(exclude_unset=True)
    if 'password' in user_dict:
        user_dict['password'] = hashpw(user.password.encode('utf-8'), gensalt()).decode('utf-8')
    result = conn.local.user.update_one(
        {"id": id},
        {"$set": user_dict}
    )

    if result.modified_count == 1:
        return userEntity(user_dict)
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

@user.get('/{id}')
async def get_user(id: int):
    user = conn.local.user.find_one({"id": id})
    if user:
        return userEntity(user)
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

@user.delete('/{id}')
async def delete_user(id: int):
    result = conn.local.user.delete_one({"id": id})

    if result.deleted_count == 1:
        return {"message": f"User with id {id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

