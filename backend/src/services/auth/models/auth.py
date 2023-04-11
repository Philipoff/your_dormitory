# from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, constr

# from backend.src.data.user import User


class RestRegister(BaseModel):
    email: EmailStr = Field(description="New user email")
    first_name: constr(min_length=1, max_length=256) = Field(description="New user firstname")
    last_name: constr(min_length=1, max_length=256) = Field(description="New user lastname")
    login: constr(min_length=1, max_length=64) = Field(description="New user login")
    password: constr(min_length=1, max_length=256) = Field(description="New user password")
#
#
# class RestCredentials(BaseModel):
#     email: EmailStr = Field(description="User email")
#     password: constr(min_length=6, max_length=55) = Field(description="User password")
#
#
# class RestTokenRefresh(BaseModel):
#     refresh: str = Field(description="Refresh JWT token")
#
#
# class RestTokenAccessRefresh(RestTokenRefresh):
#     access: str = Field(description="Access JWT token")
#
#
# class RestUser(ORMModel):
#     id: UUID = Field(description="User id")
#     email: EmailStr = Field(description="User email")
#     name: constr(min_length=1, max_length=256) = Field(description="User name")
#     role: constr(min_length=1, max_length=64) = Field(description="User role")
#     position: constr(min_length=1, max_length=256) = Field(description="User position")
#
#     @classmethod
#     def from_orm(cls, instance: User) -> "RestUser":
#         return cls(
#             id=instance.id,
#             email=instance.email,
#             name=instance.employee.name,
#             role=instance.employee.role,
#             position=instance.employee.position,
#         )
#
#
# class RestGetSetPasswordRequest(BaseModel):
#     email: EmailStr = Field(description="User email")
#     key: constr(min_length=1, max_length=256) = Field(description="Set password key")
#
#
# class RestGetSetPasswordResponse(BaseModel):
#     email: EmailStr
#
#
# class RestPostSetPasswordRequest(BaseModel):
#     email: EmailStr = Field(description="User email")
#     password: constr(min_length=6, max_length=55) = Field(description="User password")
#     key: constr(min_length=32, max_length=32) = Field(description="User set password key")
