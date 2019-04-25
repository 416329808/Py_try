
li = ["Hello world \n", "Hello China \n"]
with open('file1.txt', 'w+') as f:
    f.writelines(li)
    f.seek(0, 0)# 移动文件对象至第一个字符
    d = f.read()
# 把hello.txt 拷贝到hello2.txt
with open('file2.txt', 'a+') as dst:
    dst.write(d)
    dst.seek(0, 0)# 移动文件对象至第一个字符
    strs = dst.read()
print(strs)