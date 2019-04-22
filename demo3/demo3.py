i = 1    #循环变量
sum = 0  #求和变量
while i <= 100:
    if i % 4 == 0: #能否被四整除
        sum += i
        #print(i, end=" ")
    i += 1 #循环变量加一
print('1~100范围内能被4整除的所有数的和为', sum)
