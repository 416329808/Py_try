counter = 100 #计数变量
print('水仙花数为：')
while counter <= 999:
    list1 = list(str(counter))
    if counter == eval('pow(int(list1[0]),3)+pow(int(list1[1]),3)+pow(int(list1[2]),3)'):#若为水仙花数
        print(counter, end='\t')
    counter += 1
