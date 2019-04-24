import timeit
def get_sum():
    i = 1
    sum = 0
    while i <= 10000:
        sum += i
        i += 1

t1=timeit.timeit('get_sum()', 'from __main__ import get_sum',number=1)
print(t1)
