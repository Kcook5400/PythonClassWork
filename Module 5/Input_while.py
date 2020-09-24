"""
PEP: 8
Title: input_while
Author: Kevin Cook
Status: Active
Type: Process
Created: 23-September-2020
Post: 23-September-2020
History:
"""


flag = False
input_array = []
inputs = (input("Enter a number from 1 to 100 or type 'Exit' to quit"))
if str(inputs) == "Exit":
    exit()
while flag == False:
    try:
        if str(inputs) == "Exit":
            exit()
        if int(inputs) >= 1 or int(inputs) <= 100:
            input_array.append(inputs)
        if int(inputs) < 1 or int(inputs) > 100:
            print("That is not between 1 and 100")
        inputs = input("Enter another number or type 'Exit' to quit")
    except ValueError:
        Catch = input("That is not an integer, do you want to quit the program?")
        if Catch == "Yes":
            flag = True
        else:
            inputs = input("Enter another number or type 'Exit' to quit")
for x in input_array:
    print(x)
