def make_list():
    i=0
    input_return_list = []
    while(i<3):
        input_return_list.append(int((get_input(input = input("Enter a number")))))
        i+=1
    return input_return_list
def get_input(input):
    try:
        input_check = int(input)
        return input_check
    except ValueError:
        return "That is not a number"

