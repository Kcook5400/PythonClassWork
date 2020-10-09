


def write_to_file(tup1):
    f = open("Kevin Cook.txt", "a")
    f.write("Kevin Cook wrote here!")
    f.write('\n'+tup1)
    f.close()
def get_student_input():
    input_list = []
    input_end='y'
    while input_end == 'y':
        input1 = "Student_name={0}".format(input("Enter Student Name"))
        input2 = "Score={0}".format(input("Enter Score"))
        input3 = input1, input2
        input_list.append(tuple(input3))
        input_end = input("do you want to contine y/n?")

    write_to_file(str(input_list))
def read_from_file():
    f=open("Kevin Cook.txt", "r")
    print(f.read())
    f.close

if __name__ == '__main__':
    get_student_input()
    read_from_file()