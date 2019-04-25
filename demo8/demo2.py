import re
# 验证车牌号是否正确
plates_pha = re.compile('^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$')

while True:
    plates_number = input('请输入您的车牌号:')

    res = re.search(plates_pha, plates_number)
    if res:
        print('正常车牌号')
    else:
        print('不是车牌号')
