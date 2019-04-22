[a, b, c] = map(float, input("请依次输入长方体的长宽高,中间用空格分隔:").split()) #接收键盘输入的三个浮点数
area = 2*(a*b+b*c+a*c)      #计算表面积
vlume = a*b*c               #计算体积
print("长为%f，宽为%f，高为%f的长方体的表面积为%f" % (a, b, c, area)) #输出表面积
print("长为%f，宽为%f，高为%f的长方体的体积为%f" % (a, b, c, vlume))  #输出表面积
