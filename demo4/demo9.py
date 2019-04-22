score = {'10000': 95, '10001': 89, '10002': 87, '10003': 95, '10004': 94}
print(score)
#向字典中添加学生成绩
score['10010']=100
print(score)
#修改字典中指定学生成绩
score['10001']=99
print(score)
#删除指定学生成绩
score.pop('10000')
print(score)
#查询指定学生成绩
print("编号为10003的分数为:", score.get('10003'))
#统计学生成绩，如最高分、最低分、平均分等
print("最高分为:", max(score.values()))
print("最低分为:", min(score.values()))
print("平均分为:", sum(score.values())/len(score))