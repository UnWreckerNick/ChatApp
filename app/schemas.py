from pydantic import BaseModel, field_validator, Field
from datetime import datetime
import re

class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=32, pattern="^[A-Za-z0-9-_]+$")

class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8 or len(value) > 32:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r'\d', value):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError("Password must contain at least one special character.")
        return value

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class ChatBase(BaseModel):
    name: str

class ChatCreate(ChatBase):
    pass

class ChatResponse(ChatBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    chat_id: int

class MessageResponse(MessageBase):
    id: int
    user_id: int
    chat_id: int
    created_at: datetime

    class Config:
        from_attributes = True