"""
PEP: 8
Title: my_definitions_driver
Author: Kevin Cook
Status: Active
Type: Process
Created: 26-October-2020
Post: 26-October-2020
History:
"""
import my_definitions as defs

if __name__ == '__main__':
    defs.greeting()
    defs.author()
    d = {1: "A", 2: "B", 3: "C"}
    defs.print_dict(d)
    s = set(["C", "B", "A"])
    defs.print_set(s)
