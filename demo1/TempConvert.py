#TempConvert.py
'''

'''
Tempstr=input("请输入带有符号的温度值:")
print(Tempstr)
if Tempstr[-1] in ['F','f']:
    C=(eval(Tempstr[0:-1])-32)/1.8
    print("装换后的温度是{:.2f}C".format(C))
elif Tempstr[-1] in ['C','c']:
    F=(eval(Tempstr[0:-1])*1.8+32)
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误.")