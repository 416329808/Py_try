list1 = [3, 8, 11, 8, 11]
newList = []
for letter in list1:
    if letter not in newList:
        newList.append(letter)
print (newList)