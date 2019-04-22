#编写程序求表达式(3x+4√(x^2+2y^2 ))/(1+cosz^3 )的值
import math                                         #导入数学模块math
[x, y, z] = map(float, input("请依次输入未知数,中间用空格分隔:").split())     #接收键盘输入的三个未知数
value = (3*x+4*math.sqrt(x*x+2*y*y))/(1+math.cos(z**3))          #调用math中的相关函数计算表达式的值
print("表达式的值为:", value)
