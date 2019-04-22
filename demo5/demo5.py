def func(n):
    sum = 0
    if n % 2 == 0:
        while n >= 1:
            sum += 1/(2*n)
            n -= 2
        return sum+1/2
    else:
        while 2*n+1 >=1:
            sum += 1/(2*n+1)
            n -= 2
        return sum+1

n = 4
a = func(n)
print("前4项为:", a)