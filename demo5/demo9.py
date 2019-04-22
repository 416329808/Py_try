import math
def getTriangleC(a, b, c):
    return a+b+c
def getRectangleC(l, w):
    return 2*(l+w)
def getCircleC(r):
    return 2*math.pi*r
a = 3
b = 4
c = 5
l = 7
w = 8
r = 6
print("三边长为{0}{1}{2}的周长为{3}".format (a, b, c, getTriangleC(a, b, c)))
print("长为{0}宽为{1}的矩形周长为{2}".format(l, w, getRectangleC(l, w)))
print("半径为{0}圆的周长为{1}".format(r, getCircleC(r)))
