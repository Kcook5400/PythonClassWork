"""
PEP: 8
Title: hourly_employee_input_weekly
Author: Kevin Cook
Status: Active
Type: Process
Created: 1-October-2020
Post: 1-October-2020
History:
"""
def weekly_pay(hours_worked, pay_rate):
    """calculates weekly pay"""
    weekly_pay_total = int(hours_worked)*int(pay_rate)
    return weekly_pay_total

def hourly_employee_input():
    """ checks employee input is valid"""
    name = input("Enter your name")
    hours_worked  = input("Enter your hours worked this week in total")
    pay_rate = input("Enter your hourly rate")
    if int(hours_worked) < 0:
        raise ValueError
    if not 5 <= int(pay_rate) <= 10:
        raise ValueError
    return print("Name", str(name), "Weekly Pay $",weekly_pay(hours_worked, pay_rate))

if __name__ == "__main__":
    try:
       print(hourly_employee_input())
    except ValueError as err:
        print ("Value Error, try again")