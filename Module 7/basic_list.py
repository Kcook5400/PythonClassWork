"""
PEP: 8
Title: basic_list
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-October-2020
Post: 12-October-2020
History:
"""

def make_list():
    i=0
    input_return_list = []
    while(i<3):
        input_return_list.append(int((get_input(input = input("Enter a number")))))
        i+=1
    return input_return_list
def get_input(input):
    try:
        input_check = int(input)
        return input_check
    except ValueError:
        return "That is not a number"

