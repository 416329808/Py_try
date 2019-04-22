def isWs(n):
    l = set()
    l.add(1)
    for a in range(2, n//2):
        if n % a == 0:
            l.add(a)
            l.add(n/a)
    print(l)
    if sum(l) == n:
        return True
    else:
        return False
n = 8128
flag = isWs(n)
print(flag)
