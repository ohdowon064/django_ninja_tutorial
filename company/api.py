import pprint

from ninja import Router, Body

from company.models import Employee
from company.schema import EmployeeIn

router = Router()

@router.post("employees/")
def create_employee(request, payload: EmployeeIn = Body(...)):
    employee = Employee.objects.create(**payload.dict())
    pprint.pprint(employee.__dict__)
    return {"id": employee.id}