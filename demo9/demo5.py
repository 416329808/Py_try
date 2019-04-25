import csv
while True:
    judge=input("输入任意字符开始录入信息，-1退出:")
    if judge=='-1':
        break
    student=[]
    name=input("请输入姓名：")
    student.append(name)
    sex=input("请输入性别（男或女）：")
    student.append(sex)
    yuwen_grade=int(input("请输入语文成绩："))
    student.append(yuwen_grade)
    math_grade = int(input("请输入数学成绩："))
    student.append(math_grade)
    english_grade=int(input("请输入英语成绩："))
    student.append(english_grade)
    with open("grade_info.csv",'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(student)

#算出总成绩并且排序：
with open("grade_info.csv",'r') as f:
    reader=csv.reader(f)
    students=list(reader)
    for i in students:
        i.append(int(i[2])+int(i[3])+int(i[4]))
    students=sorted(students, key=(lambda x: x[5]), reverse=True)
    n=len(students)
    for j in range(0,n):
        students[j].append(j+1)
with open("statistics.csv",'w') as f:
    writer=csv.writer(f)
    for i in students:
        writer.writerow(i)
