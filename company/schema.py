from datetime import date
from typing import Optional

from ninja import Schema


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