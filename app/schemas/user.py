from uuid import UUID
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class ChangePassword(BaseModel):
    new_password: str
    
class UserResponse(UserBase):
    uuid: UUID
    email: EmailStr

    class Config:
        from_attributes = True