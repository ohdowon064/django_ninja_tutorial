import datetime
from typing import Optional, List, Generic, TypeVar

from ninja import Schema, Path, Field
from pydantic.fields import ModelField


class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.day)


class Filters(Schema):
    limit: int = 100
    offset: Optional[int] = None
    query: Optional[str] = None
    category__in: Optional[List[str]] = Field(None, alias="categories")


class Item(Schema):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


PydanticField = TypeVar("PydanticField")


class EmptyStrToDefault(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: PydanticField, field: ModelField) -> PydanticField:
        if value == "":
            return field.default
        return value


class ItemForm(Schema):
    name: str
    description: Optional[str] = None
    price: EmptyStrToDefault[float] = 0.0
    quantity: EmptyStrToDefault[int] = 0
    in_stock: EmptyStrToDefault[bool] = True


class UserIn(Schema):
    username: str
    password: str


class UserOut(Schema):
    id: int
    username: str


class UserSchema(Schema):
    id: int
    first_name: str
    last_name: str


class TaskSchema(Schema):
    id: int
    title: str
    is_completed: bool
    owner: Optional[str]
    lower_title: str

    @staticmethod
    def resolve_owner(obj):
        if not obj.owner:
            return
        return f"{obj.owner.first_name} {obj.owner.last_name}"

    def resolve_lower_title(self, obj):
        return self.title.lower()

class PictureSchema(Schema):
    title: str
    image: str

