from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str


class UserUpdate(BaseModel):
    name: str
    age: int
    email: str
    
class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str

    model_config = ConfigDict(from_attributes=True)