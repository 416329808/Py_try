def Fibonacci(i):
    if i == 1 or i == 2:
        return 1
    else:
        return Fibonacci(i-2)+Fibonacci(i-1)

def sum_fib10():
    i = 1
    sum = 0
    while i <= 10:
        sum += Fibonacci(i)
        i += 1
    return sum

print("数列的第十一项为：", Fibonacci(11))
print("数列的前十项和为：", sum_fib10())