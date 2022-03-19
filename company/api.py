import pprint
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Body, Path

from company.models import Employee
from company.schema import EmployeeIn, EmployeeOut

router = Router()

@router.post("employees/")
def create_employee(request, payload: EmployeeIn = Body(...)):
    employee = Employee.objects.create(**payload.dict())
    pprint.pprint(employee.__dict__)
    return {"id": employee.id}

@router.get("employees/{employee_id}/", response=EmployeeOut)
def retrieve_employee(request, employee_id: int = Path(...)):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

@router.get("employees/", response=List[EmployeeOut])
def list_employees(request):
    employee_qs = Employee.objects.all()
    return employee_qs

