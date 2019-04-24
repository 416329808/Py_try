import pandas
import numpy
df = pandas.DataFrame(numpy.random.randint(0, 10, size=[6, 4]), columns=list('ABCD'))
print('二维表格结构如下:\n', df)
print('第A列的数据为:\n', df['A'])
print('第3行的数据为:\n', df.iloc[3])
print('第3行第A列的数据为:', df.at[3, 'A'])