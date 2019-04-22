list = []
def func( n ):
    if n < 2:
        list.append(n)
        return list.reverse()
    else:
        list.append(n % 2)
        func(n//2)
n = int(input("请输入一个整数:"))
list1 = func(n)
print("{0}的二进制表示为:".format(n))
for x in list:
    print(x, end='')
