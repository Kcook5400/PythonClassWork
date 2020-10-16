


def score_input(test_score):
    test_score

    while True:
        ok_range = int(test_score)
        if int(ok_range) in range(1, 100):
            return True
        try:
            value = int(test_score)
        except ValueError:
            print("Not a number")

        attempts = attempts-1
        if attempts < 0:
            raise ValueError
        print(reminder)
    return True
