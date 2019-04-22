[a, b, c] = map(float, input("请输入三个数:").split())
if a > b:
    if a >= c and b < c:
        #print("三个数的大小顺序为", a, c, b)
        [c, b] = [b, c] #将三个数的大小顺序调整为abc
    elif c > a:
        #print("三个数的大小顺序为", c, a, b)
        [a, c] = [c, a]
        [b, c] = [c, b]#将三个数的大小顺序调整为abc
else:
    if a >= c:
        #print("三个数的大小顺序为", b, a, c)
        [a, b] = [b, a]#将三个数的大小顺序调整为abc
    elif b >= c:
        #print("三个数的大小顺序为", b, c, a)
        [a, b] = [b, a]
        [b, c] = [c, b]#将三个数的大小顺序调整为abc
    else:
        #print("三个数的大小顺序为", c, b, a)
        [a, c] = [c, a]#将三个数的大小顺序调整为abc
print("三个数的大小顺序为", a, b, c)
