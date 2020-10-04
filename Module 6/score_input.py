


def score_input(test_name, test_score):
    test_name = input("Enter your test name:")
    test_score = input("Enter your test score:")
    invalid_message = "That is not in a valid range, please try again"
    if int(test_score) not in range(0, 100):
        return invalid_message
    return test_name, test_score


