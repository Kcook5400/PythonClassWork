


def score_input(test_name, test_score=0, reminder='Invalid test score, please try again'):
    test_name
    test_score
    return test_name,test_score
    while True:
        ok_range = int(input(test_score))
        if int(ok_range) in range(1, 100):
            return test_name, test_score
        print(reminder)
