listOne = ['big', 'bad', 'wolf']
print("Printing listOne: ",listOne)

listOne.append('huffed')
print("listOne after 'huffed' is appended: ",listOne)

listOne.clear()
print("listOne cleared",listOne)

"""recreating list One after it was cleared"""
listOne = ['big', 'bad', 'wolf', 'huffed']
listTwo = listOne.copy()
print("listTwo copied from listOne: ",listTwo)

print("listOne count of 'bad': ",listOne.count('a'))

listOne.extend(listTwo)
print("listOne after extending: ",listOne)

print("listOne index of 'big': ",listOne.index('big'))

listOne.insert(0,'wolf')
print("listOne inserting 'wolf' : ",listOne)

listOne.remove('wolf')
print("listOne removing 'wolf': ",listOne)

listOne.reverse()
print("listOne reversed: ",listOne)

listOne.sort()
print("listOne sorted: ",listOne)