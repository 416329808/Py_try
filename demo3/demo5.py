counter = 0   #计数变量
for x in range(1, 5):  #百位来自1-4
    for y in range(1, 5):   #十位来自1-4
        for z in range(1, 5):   #个位来自1-4
                print("%d%d%d" % (x, y, z), end='\t')
                counter += 1
                if counter % 10 == 0:  #一行输出十个数
                    print()
print("\n能组成%d个互不相同的三位数" %( counter ))

