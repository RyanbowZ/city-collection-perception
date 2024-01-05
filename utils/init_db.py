import pymysql
import os

host = 'localhost'
db = 'city_test'
user = 'root'
#password = 'yes'


# ---- 用pymysql 操作数据库
def get_connection():
    conn = pymysql.connect(host=host, db=db, user=user)
    return conn


def check_it():

    db = pymysql.connect(
        host="localhost",
        user="root",
        #passwd="yes",
        database="city_test")

    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = db.cursor()
    SQL = """INSERT INTO user_info(user_id,user_advice) VALUES(1111111111,'红米手机')"""
    # 使用 execute()  方法执行 SQL 查询

    cursor.execute(SQL)
    db.commit()
        # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # print(data)
    # print("successfully!")

    # 使用 execute()  方法执行 SQL 查询


    # 使用 fetchone() 方法获取单条数据.

    # print("-- 当前数量: %d " % data['total'])

    # 关闭数据库连接
    db.close()


path = "../static/images/data_set_test/"


def init_image_dic():
    select_num = 0
    for i in range(0,50):
        # 对于每一个文件夹下的内容
        sql = "INSERT INTO image_dic(PID,safe,unsafe,skip,rate,P_PSID,image_name) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cur_dic = path+str(i)
        P_PSID = i
        for file in os.listdir(cur_dic):
            image_name = file.split('.')[0]
            # print(image_name)
            number = "".join(list(filter(str.isdigit, image_name)))
            if "-" in image_name:
                # print("为负的！")
                number = number+str(1)
                # print(number)
            PID = number
            # print(PID)
            safe = 0
            unsafe = 0
            skip = 0
            rate = 0
            values = (PID,safe,unsafe,skip,rate,P_PSID,image_name)
            # print(sql)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
        # print(i,"successfully!")


def init_image_set():
    select_num = 0
    for i in range(52):
        # 对于每一个文件夹下的内容
        sql = "INSERT INTO image_set(PSID,name,select_num) VALUES (%s,%s,%s)"
        PSID = i
        name = i
        values = (PSID,name,select_num)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        # print(i,"successfully!")
    # print("All successfully!")


if __name__ == '__main__':
    # init_image_set()
    init_image_dic()
    pass