set1 = {2, 5, 9, 1, 3}
set2 = {3, 6, 8, 2, 5}
#向集合set1中添加一个新的元素7
set1.add(7)
print(set1)
#求集合set1和set2的并集
print(set1 | set2)
#求集合set1和set2的交集
print(set1 & set2)
#求集合set1和set2的差集
print(set1-set2)
key = 4
print(key in set1)
print(key in set2)