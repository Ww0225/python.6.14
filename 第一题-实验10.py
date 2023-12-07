# 定义一个学生类，
# 要求：包括公共属性“总人数”和实例属性 “姓名”，私有属性“年龄”，
# 创建一个实例方法可以显示“学生姓名与年龄”，
# 一个类方法可以显示“目前学生总人数”。
# 主函数实例化几个学生对象信息，
# 并由不同的对象调用实例方法、类方法实现学生信息的设置及输出。
class student():
    total_person = 0
    def __init__(self,name,age):
        self.name = name
        self.__age = self.__setAge(age)
        student.total_person += 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age < 0:
            self.__age = 0
        self.__age = age

    def __setAge(self,age):
        if age < 0 or age > 150:
            return 0
        return age

    def getInfo(self):
        print(f"该学生的姓名为：{self.name}，年龄为：{self.age}")

    @classmethod
    def getCount(self):
        print(f"学生总人数为：{self.total_person}")

if __name__ == '__main__':
    stu1 = student('ww',18)
    stu2 = student('xx',19)
    stu1.getInfo()
    stu2.getInfo()
    student.getCount()