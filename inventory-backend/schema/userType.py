from pydantic import BaseModel, ConfigDict

# UserType Schemas
class UserTypeBase(BaseModel):
    id: int
    name: str
    description: str

class UserTypeResponse(UserTypeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)