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

def whileloop():
    input_array = []
    while input != "Exit":
        input("Enter a number from 1 to 100 or type 'Exit' to quit")
        if int(input) in range(1, 100):
            input_array.append(input)
        if int(input) not in range(1, 100):
            print("That is not between 1 and 100")

        if not input.isdigit():
            print("That is not a number")
            inputs2 = input("Do you want to exit the program?")
            if int(inputs2) == "Yes":
                exit()


    for x in input_array:
        print(x)

if __name__ == "__main__":

    whileloop()
