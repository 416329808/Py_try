#编写一个函数func(str1,str2)，将字符串str1中出现的字符串str2删除，结果存放在str1中返回
def func(str1, str2):
    str1 = str1.replace(str2, '')
    return str1

str1 = '123456haha654321hahazzzzhaha'
str2 = 'ha'
str3 = func(str1, str2)
print("去除特定字符后字符为:",str3)