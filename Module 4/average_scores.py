"""
Title: average_scores
Author: Kevin Cook
Status: Active
Type: Process
Created: 21-September-2020
Post: 121September-2020
History:
"""


def average(score1, score2, score3):
    a = [score1,score2,score3]
    NUMBER_TESTS = 3
    for x in a:
        if x < 0:
            raise ValueError
    return (score1 + score2 + score3)/NUMBER_TESTS


if __name__ == '__main__':
    # program to run
    score1 = int(input("Enter score 1"))
    score2 = int(input("Enter score 2"))
    score3 = int(input("Enter score 3"))
    try:
        print("Your average score is: ", average(score1, score2, score3))
    except:
        raise ValueError