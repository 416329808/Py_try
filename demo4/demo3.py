list1 = [3, 8, 11, 26, 47]
a = int(input("请输入一个key:"))
i = 0
while i < list1.__len__():
    if list1[list1.__len__()-1] <= a:
        list1.append(a)
        break
    elif list1[i] > a:
        list1.insert(i, a)
        break
    i += 1
print(list1)