#! /usr/bin/python3
from chapter11 import Employee
import pytest
def test_give_default_raise():
    employee = Employee("Wanda", "Worthy", 90000)
    employee.give_raise()
    assert employee.salary == 95000
    
def test_give_custom_raise():
    employee = Employee("Wanda", "Worthy", 90000)
    employee.give_raise(2000)
    assert employee.salary == 92000
    
#same thing, with fixture
@pytest.fixture
def employee_test():
    employee = Employee("Wanda", "Worthy", 90000)
    return employee

def test_give_default_raise2(employee_test):
    employee_test.give_raise()
    assert employee_test.salary == 95000
    
def test_give_custom_raise2(employee_test):
    employee_test.give_raise(2000)
    assert employee_test.salary == 92000
