def digui(n):
    if n == 1:
        return 10
    else:
        return digui(n-1)+2
def old(n):
    return (n-1)*2+10

n = 5
a = digui(n)
b = old(n)
print("递归:", a)
print("非递归:", b)
