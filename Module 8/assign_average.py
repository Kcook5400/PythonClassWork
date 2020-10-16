
def switch_average(test):
    if test not in {'A', 'B', 'C', 'D'}:
        raise ValueError
    return{
        "A": 1,
        'B': 2,
        'C': 3,
        'D': 4
    }[test]

