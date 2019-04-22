m_money = 1*10**5*30#陌生人给富翁总钱数
day = 1#计日期变量
f_money_sum = 0
f_money = 0.01
while day <= 30:
    f_money = f_money*2#富翁每天给陌生人的钱数
    f_money_sum += f_money#富翁陌生人的钱数求和
    day += 1
print('陌生人给富翁总钱数', m_money)
print('富翁给陌生人总钱数', f_money_sum)
