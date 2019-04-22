#编写一个函数func(str)，计算并返回传入字符串中的数字、字母以及其它类型字符的个数
def func(str):
    i = 0
    j = 0
    k = 0
    for x in str:
        if x <= '9' and x >= '0' :
            i += 1
        elif x <= 'z' and x >= 'a' or x <='Z' and x >='A':
            j += 1
        else:
            k += 1
    list1 = [i, j ,k]
    return  list1
str = "12345678909ABCDEFGHIJKlmnopqrstuvwxyz.,/'\][;-="
list = func(str)
print("数字字母其他字符的个数分别为:")
for x in list:
    print(x)