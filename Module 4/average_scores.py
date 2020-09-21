"""
Title: average_scores
Author: Kevin Cook
Status: Active
Type: Process
Created: 13-September-2020
Post: 13-September-2020
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
    average_score = average(score1, score2, score3)
    print("Your average score is: ", str(average_score))
