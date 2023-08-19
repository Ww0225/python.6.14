class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self):
        print(f"大家好，我是{self.name},很高兴认识大家")

stu_1 = Student()

stu_1.name = "ww"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "广东省"
stu_1.age = 21
stu_1.say_hi()
