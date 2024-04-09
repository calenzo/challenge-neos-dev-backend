from pydantic import BaseModel


class AuthRegister(BaseModel):
    username: str
    password1: str
    password2: str


class AuthLogin(BaseModel):
    username: str
    password: str
