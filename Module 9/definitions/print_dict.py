"""
PEP: 8
Title: print_dict
Author: Kevin Cook
Status: Active
Type: Process
Created: 26-October-2020
Post: 12-October-2020
History:
"""
def print_dict(this_dict):
    for x in this_dict:
        print("Key:", x, "Data:", this_dict[x])