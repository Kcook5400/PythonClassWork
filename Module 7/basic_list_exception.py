def make_list():
    i=1
    input_return_list = []
    while (i <4):
        value = input("Enter a number")
        if value in range(1, 50):
            input_return_list.append(int((get_input(value))))
            i += 1
        else:
            raise ValueError
    return input_return_list

def get_input(value):
    try:
        input_check = int(value)
        return input_check
    except ValueError:
        return"That is not a number"


