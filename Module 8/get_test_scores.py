"""
PEP: 8
Title: dictionary_update_assignment
Author: Kevin Cook
Status: Active
Type: Process
Created: 15-October-2020
Post: 12-October-2020
History:
"""


def score_input(test_score):
    try:
        int(test_score) in range(1, 100)
        value = int(test_score)
    except ValueError:
        print("Not a number or not in range 1-100")
        return False
    if int(test_score)  not in range(1, 100):
        print("Score not between 1 and 100")
        return False
    return True

def get_test_scores():
    scores_dict = dict()
    num_scores = input("Enter number of test scores")
    for x in range(0, int(num_scores)):
        scores = input("input test scores")
        if score_input(scores) != True:
            exit()
        scores_dict[x]= int(scores)
    return scores_dict

def average_scores(scores_dict):
    dict_length = len(scores_dict)
    total = sum(scores_dict.values())
    average = total/dict_length
    print("The average test score is", average)



if __name__ == '__main__':
    scores_dict = get_test_scores()
    average_scores(scores_dict)