"""
PEP: 8
Title: search_and_sort_array
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-October-2020
Post: 12-October-2020
History:
"""
import array as arr


def search_list(search_letter):
    a = arr.array('i',[1,3,4,5,6,7,8])
    list_a = a.tolist()
    if search_letter in list_a:
        return list_a.index(search_letter)
    else:
        return -1


def sort_list():
    a = arr.array('i', [1, 3, 4, 5, 6, 7, 8])
    list_a = a.tolist()
    list_a.sort(reverse=True)
    return list_a
