# def encode(x):
#     return (x+5) % 10

str = input("请输入四位整数:")  #接收键盘输入的一个四位整数
if str.__len__() != 4:
    print("请输入的一个四位整数")
else:
    a = (int(str[0])+5) % 10    #强转为整形数字都加上5，然后用和除以10的余数代替该数字
    b = (int(str[1])+5) % 10
    c = (int(str[2])+5) % 10
    d = (int(str[3])+5) % 10
# for number in range(len(str)):
#     list1 = int(str[number])
# list = map(encode, list1)23
# print(list)
    print("替换后数字为:", a, b, c, d)
    [a, d] = [d, a]  #第一位和第四位交换
    [b, c] = [c, b]  #第二位和第三位交换
    print("加密后的数字:", a, b, c, d)
