


def score_input(test_name, test_score=0, attempts=3, reminder='Invalid test score, please try again'):
    test_name
    test_score

    while True:
        ok_range = int(test_score)
        if int(ok_range) in range(1, 100):
            return test_name, test_score
        attempts = attempts-1
        if attempts < 0:
            raise ValueError
        print(reminder)
    return test_name, test_score
