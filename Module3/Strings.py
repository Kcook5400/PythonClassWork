"""
PEP: 8
Title: Strings
Author: Kevin Cook
Status: Active
Type: Process
Created: 13-September-2020
Post: 13-September-2020
History:
"""

name = "The Hulk in the Avengers"

print(name.capitalize())
print(name.find('Hulk'))
namesplit = name.split()
print(namesplit.index('Hulk'))
print(name.isalnum())
print(name.isalpha())
print(name.isdigit())
print(name.islower())
print(name.isupper())
print(name.isspace())
print(name.startswith('T'))