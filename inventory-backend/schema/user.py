from pydantic import BaseModel

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    user_type_id: int

class UserResponse(UserBase):
    id: int
    user_type: str

class UserAuth(BaseModel):
    username: str
    password: str