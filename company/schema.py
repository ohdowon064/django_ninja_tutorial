from datetime import date
from typing import Optional

from django.conf import settings
from django.contrib.auth.models import User
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
        model = User
        model_exclude = ["password", "last_login", "user_permissions"]
