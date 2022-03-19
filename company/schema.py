from datetime import date
from typing import Optional

from django.conf import settings
from ninja import Schema, ModelSchema


class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: Optional[int] = None
    birthdate: Optional[date] = None


class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: Optional[int] = None
    birthdate: Optional[date] = None


class UserSchema(ModelSchema):
    class Config:
        model = settings.AUTH_USER_MODEL
        model_exclude = ["password", "last_login", "user_permissions"]
