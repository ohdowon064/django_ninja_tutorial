import datetime
from typing import Optional, List

from ninja import Schema, Path
from pydantic import Field


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

