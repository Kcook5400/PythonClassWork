"""
PEP: 8
Title: employee
Author: Kevin Cook
Status: Active
Type: Process
Created: 11-1-2020
Post: 11-1-2020
History:
"""
from numpy import double


class Employee:
    def __init__(self, last_name, first_name, address, phone_number, salaried, start_date, salary):
        self.last_name = str(last_name)
        self.first_name = str(first_name)
        self.address = str(address)
        self.phone_number = str(phone_number)
        self.salaried = bool(salaried)
        self.start_date = str(start_date)
        self.salary = double(salary)
    def display(self):
        print(self.first_name, self.last_name)
        print(self.address)
        if self.salaried == True:
            print("Salaried Employee: ", self.salary)
        elif self.salaried == False:
            print ("Hourly Employee: $7.25/hour")
        print(self.start_date)

Emp=Employee("doe","jon","123 fake st","555-555-5555",True,"2020, 11, 11",200)
Emp2=Employee("doe","jon","123 fake st","555-555-5555",False,"2020, 11, 11",200)
Emp.display()
Emp2.display()