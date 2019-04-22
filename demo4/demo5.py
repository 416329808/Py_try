import numpy
list1 = numpy.random.randint(0, 11, 20)
tuple = tuple(list1)
print(tuple)
newList = []
for letter in tuple:
    if letter not in newList:
        newList.append(letter)
newList.sort()
for letter in newList:
    print("%d出现的个数为%d " % (letter , tuple.count(letter)))