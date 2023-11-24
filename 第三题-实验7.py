# 假设成年人的体重和身高存在此种关系：身高（厘米）-100=标准体重（千克）
# 如果一个人的体重与其标准体重的差值在正负5之间，显示“体重正常”，高于标准体重则显示“体重超标”，低于标准体重显示“体重不达标”。
# 编写程序：
# (1) 自定义异常,处理身高小于50cm、大于250cm的异常情况。
# (2) 主函数中输入身高与体重，并对用户输入数据判断，使用assert、raise抛出异常，并对抛出的异常进行处理。
class HighException(Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return f"异常：{self.message}"

def check_weight(height,weight):
    try:
        if height < 50 or height > 250:
            raise HighException("身高异常")
        standard_weight = height-100
        weight_difference = weight-standard_weight
        if abs(weight_difference)<= 5:
            print("体重正常")
        elif weight > standard_weight:
            print("体重超标")
        else:
            print("体重不达标")
    except HighException as e:
        print(e)

try:
    height = int(input("请输入身高（单位：厘米）："))
    weight = float(input("请输入体重（单位：千克）："))
    check_weight(height,weight)
except ValueError:
    print("输入格式错误，请输入有效的身高和体重。")

