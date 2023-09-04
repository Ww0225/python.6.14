from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="Wew18948459936",
    autocommit=True
)

# print(conn.get_server_info())

cursor = conn.cursor()

conn.select_db("sys")

# cursor.execute("create table test_pymysql(id int)")

cursor.execute("insert into student values(1002,'cc',44)")

# results = cursor.fetchall()
# print(results)
# conn.commit()

conn.close()