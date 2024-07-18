# import pymongo
#serializer

# def userEntity(item)->dict: # for single doc
#    return{
#       "id":str(item["_id"]),
#       "name":item["name"],
#       "email":item["email"],
#       "password":item["password"]
#    }



# def usersEntity(entity):
#     if isinstance(entity, pymongo.collection.Collection):
#         entity = list(entity.find())  # Convert Collection to list of documents
#     return [userEntity(item) for item in entity]


# schemas/user.py

import pymongo

def userEntity(item) -> dict:
    return {
        "id": item["id"],  # Assuming "id" is stored as an integer in MongoDB
        "name": item["name"],
        "email": item["email"],
        "mobile_number":item["mobile_number"],
        "location":item["location"],
        # "password": item["password"]
    }

def usersEntity(entity):
    if isinstance(entity, pymongo.collection.Collection):
        entity = list(entity.find())  # Convert Collection to list of documents
    return [userEntity(item) for item in entity]
