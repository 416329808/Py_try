with open('gch.txt','w+') as f:
    f.write("""《观沧海》 -曹操
东临碣石，以观沧海。
水何澹澹，山岛竦峙。
树木丛生，百草丰茂。
秋风萧瑟，洪波涌起。
日月之行，若出其中。
星汉灿烂，若出其里。
幸甚至哉，歌以咏志。""")
    f.seek(0, 0)# 移动文件对象至第一个字符
    d = f.read()
print(d)
