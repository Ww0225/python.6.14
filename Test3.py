print("1 + 1 = ",1 + 1)
print("2 - 1 = ",2 - 1)
print("3 * 3 = ",3 * 3)
print("4 / 2 = ",4 / 2)
print("11 // 2 = ",11 // 2)
print("9 % 2 = ",9 % 2)
print("2 ** 2 = ",2 ** 2)

name = "黑马程序员"
massage = "学IT来： %s " % name
print(massage)

class_num = 57
avg_salary = 18888
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num,avg_salary)
print(message)

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度是2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度是2，结果是：%.2f" % num2)

name = "传智播客"   #公司名
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司{name},股票代码:{stock_code},当前股价{stock_price}")
print("每日增长系数是：%.1f,经过%d的增长后,股价达到了:%.2f" % (stock_price_daily_growth_factor,growth_days,finally_stock_price))

name = input("请告诉我你是谁？")
print("我知道了，你是：%s" % name)

user_name = input()
user_type = input()
print(f"您好：{user_name},您是尊贵的：{user_type} 用户，欢迎您的光临")