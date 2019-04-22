import math
while 1 == 1:
    str1 = int(input("请输入不多于五位的正整数:"))
    list1 = list(str(str1))         #将字符串强转列表
    if list1.__len__() <= 5 and str1 > 0:   #判断位数是否为五位的正整数
        print("%s的位数为%d位" % (str1, list1.__len__())) #输出数字的位数
        list1.reverse()             #将列表逆置
        it = iter(list1)            #将列表强转为迭代器
        for x in it:
            print(x, end=" ")

        # counter = -1
        # while math.fabs(counter) <= list1.__len__():
        #     print(list1[counter], end=" ")
        #     counter -= 1
        break
