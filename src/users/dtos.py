from pydantic import BaseModel, EmailStr
from pydantic import field_validator

class UserSchema(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

    @field_validator("name", "username", "password")
    @classmethod
    def reject_blank(cls, value):
        if not value.strip():
            raise ValueError("Field cannot be empty")
        return value

    
class UserResponseSchema(BaseModel):
    name: str
    username: str
    email: str
    id: int

class LoginSchema(BaseModel):
    username: str
    password: str