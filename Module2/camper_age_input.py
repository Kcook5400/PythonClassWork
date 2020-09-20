"""
PEP: 8
Title: camper_age_input
Author: Kevin Cook
Status: Active
Type: Process
Created: 06-September-2020
Post: 06-September-2020
History:
"""


def convert_to_months(age_in_years):

 return age_in_years*12 # code to calculate age in months


if __name__ == '__main__':
#program to run
    age_in_years = int(input("Enter your age in years"))
    age_in_months = convert_to_months(age_in_years)
    print(age_in_months)