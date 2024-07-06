# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from pymongo.collection import Collection
# from config.db import conn
# from bcrypt import hashpw, gensalt

# password_reset_router = APIRouter(prefix="/password_reset",tags=['Password Reset'])

# class PasswordResetRequest(BaseModel):
#     email: str
#     new_password: str

# @password_reset_router.put('/')
# async def reset_password(request: PasswordResetRequest):
#     user_collection: Collection = conn.local.user
#     user = user_collection.find_one({"email": request.email})
    
#     if user:
#         new_hashed_password = hashpw(request.new_password.encode('utf-8'), gensalt()).decode('utf-8')
#         result = user_collection.update_one(
#             {"email": request.email},
#             {"$set": {"password": new_hashed_password}}
#         )
        
#         if result.modified_count == 1:
#             return {"message": "Password reset successful"}
#         else:
#             raise HTTPException(status_code=500, detail="Password reset failed")
#     else:
#         raise HTTPException(status_code=404, detail="User with the given email not found")


from fastapi import APIRouter, HTTPException
from pymongo.collection import Collection
from config.db import conn
from models.password_reset import PasswordResetRequest
from bcrypt import hashpw, gensalt

password_reset_router = APIRouter(prefix="/api/v1/password_reset", tags=['Password Reset'])


@password_reset_router.put('/{email}')
async def reset_password(email: str,request: PasswordResetRequest):
    user_collection: Collection = conn.local.user
    user = user_collection.find_one({"email": email})
    
    if user:
        new_hashed_password = hashpw(request.new_password.encode('utf-8'), gensalt()).decode('utf-8')
        result = user_collection.update_one(
            {"email": email},
            {"$set": {"password": new_hashed_password}}
        )
        
        if result.modified_count == 1:
            return {"message": "Password reset successful"}
        else:
            raise HTTPException(status_code=500, detail="Password reset failed")
    else:
        raise HTTPException(status_code=404, detail="User with the given email not found")
    


