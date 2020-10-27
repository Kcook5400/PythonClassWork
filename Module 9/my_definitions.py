"""
PEP: 8
Title: my_definitions
Author: Kevin Cook
Status: Active
Type: Process
Created: 26-October-2020
Post: 26-October-2020
History:
"""
def greeting():
    print("Hello and Welcome")
def author():
    print("Kevin Cook is the author of this code")
def print_dict(this_dict):
    for x in this_dict:
        print("Key:", x, "Data:", this_dict[x])
def print_set(setA):
    for x in set(setA):
        print(x, end=" ")

