class Student:
    name = None
    age = None
    address = None

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

students = []
for i in range(1,11):
    name = input(f"当前录入第{i}位学生信息，总共需录入10位学生信息\n请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    address = input("请输入学生地址：")
    student = Student(name,age,address)
    students.append(student)
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{student.name},年龄：{student.age},地址：{student.address}】")
