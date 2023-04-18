from pydantic import BaseModel, EmailStr, Field, constr


class RestRegister(BaseModel):
    email: EmailStr = Field(description="New user email")
    login: constr(min_length=1, max_length=64) = Field(description="New user login")
    password: constr(min_length=1, max_length=256) = Field(description="New user password")


class RestLogin(BaseModel):
    email: EmailStr = Field(description="Login e-mail")
    password: constr(min_length=1, max_length=256) = Field(description="Login password")
