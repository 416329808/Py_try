def isGDBH(n):
    i = 2
    list = []
    list1 = []
    while i <= n:
        if(Isprime(i)):
            list.append(i)
        i += 1
    if list.__len__() > 1:
        for x in list:
            for y in list:
                if (x + y == n) and x <= y:
                    str1 = str(x)+"+"+str(y)+"="+str(n)
                    list1.append(str1)
    return list1

def Isprime(i):  #自定义函数是否为素数
    j = 2
    flag = True  #标志变量
    while j <= i/2:
        if i % j == 0:
            flag = False  #若存在1和本身以外其它因数则不为素数
            break
        j += 1
    return flag

list = isGDBH(14)
print(list)
