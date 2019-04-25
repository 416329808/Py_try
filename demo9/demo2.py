import random
import math
with open('sjs.txt', 'w') as f:
    for i in range(0, 20):
        sjs=random.randint(0, 100)
        f.write(str(sjs)+'\n')
list1 = []
with open('sjs.txt', 'r') as f2:
    for i in range(0, 20):
        num=int(f2.readline())
        list1.append(num)
sum= 0
for i in list1:
    sum += i
aver = sum/20
variance = 0
sum2 = 0
for i in list1:
    sum2 += (i-aver)*(i-aver)
variance = math.sqrt(sum2/20)
print("方差为", variance)
