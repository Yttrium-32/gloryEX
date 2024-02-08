from pydantic import BaseModel

from .skills import SkillPublic

class UserBase(BaseModel):
    username: str
    email: str

class UserRequestDetails(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    password: str

class UserDelete(BaseModel):
    username: str
    # password: str

class UserPublic(UserBase):
    id: int
    skills: list[SkillPublic] = []
    class Config:
        from_attributes = True

class UserVerifySuccess(UserBase):
    id: int
    class Config:
        from_attributes = True

