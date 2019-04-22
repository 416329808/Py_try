i = 1
while i <= 4:
    j = 4 - i
    while j > 0:
        print(" ", end="\t") #第i行先输出4-i空格
        j -= 1
    p = 2*i - 1
    while p > 0:
        print("*", end="\t")#第i行先输出2*i - 1个*
        p -= 1
    i += 1
    print()
