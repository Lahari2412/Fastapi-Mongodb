from pydantic import BaseModel

class PasswordResetRequest(BaseModel):
    new_password: str