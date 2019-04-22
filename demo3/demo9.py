number = 13*10**8 #初始值13亿
sum = number    #总人数为初始值
counter = 0
while sum <= 20*10**8:
    sum += sum*0.8/100  #总人数上一年加增长率
    counter += 1
print('%d年后我国人口超过20亿' % (counter))