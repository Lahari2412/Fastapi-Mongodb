from fastapi import FastAPI
from routes.user import user
from routes.login_router import login_router
from routes.password_reset import password_reset_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://localhost:8000" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(login_router)
app.include_router(password_reset_router)

