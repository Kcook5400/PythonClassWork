"""
PEP: 8
Title: basic_list
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-October-2020
Post: 12-October-2020
History:
"""
def average_scores(*args, **kwargs):
    total = 0
    for x in args:
        total = total + x
    average = total / len(args)
    # Use *args for average calculation
    out = ""
    for key, value in kwargs.items():
        out = out + (("%s == %s" % (key, value)))
    print(out, " Average Score", average)


if __name__ == '__main__':
    (average_scores(4, 1, 5, 6, name='Kevin ', gpa=3.0, course='Python '))
    (average_scores(4, 2, 9, name='Kevin ', Program='Computer Science ', course='Python '))
    (average_scores(4, 3, 3, 6, 7, 8, 9, name='Kevin ', last_name ='Cook ', state='Iowa '))