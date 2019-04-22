import numpy
list1 = numpy.random.randint(0, 101, 10)
print(list1)
i = 0
while i < list1.__len__():
    if i % 2 == 0:
        list1[i] **= 2
    else:
        list1[i] **= 3
    i += 1
print(list1)