a = 6
str1 = 'hello world'
list = ['tom', 'john', 'jack']
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
with open('b_file.dat', 'wb+') as f1:
    f1.write(str(a).encode('utf-8'))
    f1.write(str1.encode('utf-8'))
    f1.write(str(list).encode('utf-8'))
    f1.write(str(dict).encode('utf-8'))
    f1.write(str(basket).encode('utf-8'))
    f1.seek(0, 0)# 移动文件对象至第一个字符
    string = f1.read()
print(string)
