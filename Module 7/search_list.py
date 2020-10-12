def search_list(search_letter):
    list_a = ['A', 'B', 'C', 'D', 'E']
    if search_letter in list_a:
        return list_a.index(search_letter)
    else:
        return -1

def sort_list():
    list_a = [1, 3, 4, 2, 5]
    list_a.sort(reverse=True)
    return list_a
