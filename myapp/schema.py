import datetime
from typing import Optional, List, Generic, TypeVar

from ninja import Schema, Path
from pydantic import Field
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
        print("get_validator 호출됨")
        yield cls.validate

    @classmethod
    def validate(cls, value: PydanticField, field: ModelField) -> PydanticField:
        print("validate 호출됨")
        if value == "":
            return field.default
        return value

class ItemForm(Schema):
    name: str
    description: Optional[str] = None
    price: EmptyStrToDefault[float] = 0.0
    quantity: EmptyStrToDefault[int] = 0
    in_stock: EmptyStrToDefault[bool] = True