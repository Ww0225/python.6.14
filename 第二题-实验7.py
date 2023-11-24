# 从输入端中获取成绩，并对输入的内容进行异常处理：
# （1）输入数值，但不在(1--100)，显示“请输入0-100之间的数”；
# （2）如果输入类型不是数值，显示“类型有误，请重新输入”。
# （3）输入的数据符合要求，则输出对应的等级（90-100为A，80-89为B,70-79为C，60-69为D，60以下为E）。
# 操作方法与步骤：
# 创建Test2.py程序，输入成绩score,并使用re模块对输入的score进行判断，
# 是否为数值，如果是数值，则使用if.....else多分支进行处理并输出成绩等级，
# 如果不是数值，则进行“类型有误，请重新输入”提示处理。

while True:
    try:
        score = int(input("请输入你的成绩："))
        assert score >= 0 and score <= 100, "请输入0-100之间的数："
    except ValueError:
        print("类型有误，请重新输入")
    except AssertionError as reason:
        print(reason)
    else:
        if score >= 90:
            print("成绩为：A")
        elif score >= 80 and score <= 89:
            print("成绩为：B")
        elif score >= 70 and score <= 79:
            print("成绩为：C")
        elif score >= 60 and score <= 69:
            print("成绩为：D")
        else:
            print("成绩为：E")
        break

# 参考答案
# import re
# while True:
#     score = input("请输入你的成绩：")
#     value = re.compile(r'^[+-]?[0-9]+[.]?[0-9]*$')
#     try:
#         assert value.match(score), "输入的不是数字，请重新输入！"
#         score = eval(score)
#         assert score >= 0 and score <= 100, "成绩范围0-100，请重新输入！"
#         if score >= 90:
#             print("成绩为：A")
#         elif score >= 80 and score <= 89:
#             print("成绩为：B")
#         elif score >= 60 and score <= 79:
#             print("成绩为：C")
#         else:
#             print("成绩为：D，不及格！！！")
#     except AssertionError as reason:
#         print(reason)