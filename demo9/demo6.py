with open('a.txt', 'r') as f1:
    a = f1.read()
with open('b.txt', 'r') as f2:
    b = f2.read()
print(a)
print(b)
c = list(a+b)
c.sort()
with open('c.txt', 'w+') as f3:
    f3.write(''.join(c))
    f3.seek(0, 0)# 移动文件对象至第一个字符
    d = f3.read()
print(d)