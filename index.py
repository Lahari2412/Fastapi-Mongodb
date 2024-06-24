from fastapi import FastAPI
from routes.user import user
from routes.login_router import login_router

app=FastAPI()

app.include_router(user)
app.include_router(login_router)
