Max = 10
Min = 0

y = 8

if int(y) > Max:
    print(str(y) + " is greater than " + str(Max))
else:
    print(str(y) + " is less than " + str(Max))
if  int(y) < Min:
    print(str(y) + " is less than " + str(Min))
else:
    print(str(y) + " is greater than " + str(Min))

x = 9
if Min < int(x) < Max and int(x) != Min and int(x) != Max:
    print (str(x) + " is between " + str(Min) + " and " + str(Max) + " but not " + str(Min) + " or " + str(Max))
if Min < int(x) < Max and int(x) != Max:
    print (str(x) + " is between " + str(Min) + " and " + str(Max) + " but not equal to " + str(Max))
if Min < int(x) <= Max:
    print (str(x) + " is between " + str(Min) + " and " + str(Max) + ",including " + (str(Max)))