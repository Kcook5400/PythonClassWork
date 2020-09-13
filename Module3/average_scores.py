"""
Title: average_scores
Author: Kevin Cook
Status: Active
Type: Process
Created: 13-September-2020
Post: 13-September-2020
History:
"""


def average():
    score1 = int(input("Enter 1st Score"))
    score2 = int(input("Enter 2nd Score"))
    score3 = int(input("Enter 3rd Score"))
    average = (score1 + score2 + score3) / 3
    str(average)
    return average


if __name__ == '__main__':
    # program to run
    name_first = str(input("Enter your first name"))
    name_last = str(input("Enter your last name"))
    age = str(input("Enter your age"))
    average_score = average()
    print("First Name:", name_first)
    print("Last Name:", name_last)
    print("Your average score is: ", average_score)
