from fastapi import FastAPI
from pydantic import BaseModel

class Emp(BaseModel):
    id: int
    name: str
    salary: float

proj = FastAPI()

employees = {}

@proj.get("/emp/{emp_id}")
def get_emp_by_id(emp_id: int):
    if emp_id not in employees:
        return "Employee not found"
    return employees[emp_id]

@proj.post("/emp")
def add_emp(emp_id: int, emp: Emp):
    if emp_id in employees:
        return "Employee already exists"
    employees[emp_id] = emp
    return "Employee Added"

@proj.delete("/emp/{emp_id}")
def del_emp(emp_id: int):
    if emp_id not in employees:
        return "Employee not found"
    del employees[emp_id]
    return "Employee Deleted"

@proj.put("/emp/{emp_id}")
def update_emp(emp_id: int, emp: Emp):
    if emp_id not in employees:
        return "Employee not found"
    employees[emp_id] = emp
    return "Employee Updated"