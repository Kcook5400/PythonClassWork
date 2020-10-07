"""
PEP: 8
Title: hourly_employee_input
Author: Kevin Cook
Status: Active
Type: Process
Created: 30-September-2020
Post: 30-September-2020
History:
"""


def hourly_employee_input():
    """ checks employee input is valid"""
    name = input("Enter your name")
    hours_worked  = input("Enter your hours worked")
    pay_rate = input("Enter your hourly rate")
    if int(hours_worked) < 0:
        raise ValueError
    if not 5 <= int(pay_rate) <= 10:
        raise ValueError
    print("Employee Name" , str(name),"\nHours Worked", int(hours_worked),"\nPay Rate", float(pay_rate))

if __name__ == "__main__":
    try:
        hourly_employee_input()
    except ValueError as err:
        print ("Value Error, try again")