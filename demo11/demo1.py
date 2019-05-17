import sqlite3

def create():
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    sql = '''create table tb_grade (sno int primary key not null, sname varchar(20), sex varchar(10), brithday date, maths int, english int, os int)'''
    try:
        # 执行SQL语句
        c.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        print("Error: unable to Create table")
    conn.close()


def insert(grade):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    try:
        # 执行SQL语句
        c.executemany('insert into tb_grade values (?,?,?,?,?,?,?)', grade)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        print("Error: unable to insert data")
    conn.close()

def selectall():
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()

    try:
        # 执行SQL语句
        c.execute('select * from tb_grade')
        # 获取所有记录列表
        conn.commit()
        results = c.fetchall()

    except:
        print("Error: unable to fetch data")


    for row in results:
        sno = row[0]
        sname = row[1]
        sex = row[2]
        birthday = row[3]
        maths = row[4]
        english = row[5]
        os = row[6]
        # 打印结果
        print("sno =%s,sname=%s,sex=%s,birthday=%s,maths=%s,english=%s, os=%s" % (
            sno, sname, sex, birthday, maths, english, os))

        # 关闭数据库连接
    conn.close()

def update(date):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    try:
        # 执行SQL语句
        c.execute('update tb_grade set maths = ? where sno = ?', date)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        print("Error: unable to update data")
    conn.close()

def delete(date):
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    try:
        # 执行SQL语句
        c.execute('delete from tb_grade where sno = ? ', date)
        # 提交修改
        conn.commit()
        # 发生错误时回滚
    except:
        conn.rollback()
        print("Error: unable to delete data")
    conn.close()

grade = [(1, 'mark', 'male', '2000-05-20', 99, 80, 85),
            (3, 'tom', 'male', '2000-06-09', 90, 85, 87),
            (4, 'jack', 'female', '2000-06-09', 87, 90, 90),
            (5, 'ming', 'male', '2000-06-09', 82, 82, 70)]
udate = (100, 1,)
ddate = (5,)
create()
insert(grade)
print('插入数据')
selectall()
update(udate)
print('更新学号为1的数学成绩为100')
selectall()
delete(ddate)
print('删除学号为5的信息')
selectall()



