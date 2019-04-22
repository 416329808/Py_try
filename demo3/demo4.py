def Isprime(i):  #自定义函数是否为素数
    j = 2
    flag = True  #标志变量
    while j <= i/2:
        if i % j == 0:
            flag = False  #若存在1和本身以外其它因数则不为素数
            break
        j += 1
    return flag

counter = 101
print('101-200之间的所有素数为')
while counter <= 200:
    flag1 = Isprime(counter)
    if flag1 == True:      #若为素数，则输出
        print(counter, end=" ")
    counter += 1
