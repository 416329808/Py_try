import os
import os.path
print(os.getcwd())      #打印当前目录
print([fname for fname in os.listdir(os.getcwd())])     #当前目录下所有文件名