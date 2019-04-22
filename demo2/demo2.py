#编写程序求解方程x^2+4x+3=0
import math
[a, b, c] = map(float, input("请依次输入系数,中间用空格分隔:").split())  #接收键盘输入的三个系数
de = b*b-4*a*c                  #求判别式
if de < 0:                      #判别式小于0，无实根
    print("此方程无实数根")
elif de == 0:                   #判别式等于0，有两个相等的实根
    x = (-1*b)/2*a              #求根公式
    print("此方程有唯一的实数根x,x=", x)
else:                           #判别式大于0，有两个不等的实根
    x1 = (-1*b+math.sqrt(de))/2*a
    x2 = (-1*b-math.sqrt(de))/2*a
    print("此方程存在两个不等的实根,两个根为:x1=%f,x2=%f" % (x1, x2))

