import pymysql


def insert(info):
    # 打开数据库连接
    db = pymysql.connect(host="localhost", db="employee_info", user="root", password="root")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO tb_emp(eid, ename, sex, birthday, intro, profession, dept)
             VALUES (%s, %s, %s, %s, %s, %s, %s )"""
    try:
        # 执行SQL语句
        cursor.executemany(sql, info)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        print("Error: unable to insert data")

    # 关闭数据库连接
    db.close()


def selectall():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", db="employee_info", user="root", password="root")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM tb_emp ;"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except:
        print("Error: unable to fetch data")


    for row in results:
        eid = row[0]
        name = row[1]
        sex = row[2]
        birthday = row[3]
        intro = row[4]
        profession = row[5]
        dept = row[6]
            # 打印结果
        print("eid=%s,name=%s,sex=%s,brithday=%s,intro=%s,profession=%s, dept=%s" % (
                eid, name, sex, birthday, intro, profession, dept))
    # 关闭数据库连接
    db.close()


def delete(data):
    # 打开数据库连接
    db = pymysql.connect(host="localhost", db="employee_info", user="root", password="root")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM tb_emp WHERE eid = %s ;"
    try:
        # 执行SQL语句
        cursor.execute(sql, data)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        print("Error: unable to delete data")

    # 关闭连接
    db.close()


def update(data):
    # 打开数据库连接
    db = pymysql.connect(host="localhost", db="employee_info", user="root", password="root")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE tb_emp SET intro = %s WHERE eid = %s"
    try:
        # 执行SQL语句
        cursor.execute(sql, data)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        print("Error: unable to update data")

    # 关闭数据库连接
    db.close()


info = [('1', 'mark', 'male', '2000-05-20', 'Chinese', '100000', '10000'),
        ('3', 'tom', 'male', '2000-06-09', 'Chinese', '100001', '10001'),
        ('4', 'jack', 'female', '2000-06-09', 'Chinese', '100002', '10002'),
        ('5', 'ming', 'male', '2000-06-09', 'Chinese', '100000', '10001')]

updata = ('hubeiwuhan', '5', )

dedata = ('4',)

print('插入数据')
insert(info)
selectall()
print('更新工号为5的intro')
update(updata)
selectall()
print('删除工号为4的信息')
delete(dedata)
selectall()

