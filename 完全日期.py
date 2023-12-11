# 如果一个日期中年月日的各位数字之和是完全平方数，则称为一个完全日期。
# 例如：2021年6月5日的各位数字之和为2+0+2+1+6+5=16，而 16是一个完全平方数，它是4的平方。所以 2021年6月5日是一个完全日期。
# 例如：2021年6月23日的各位数字之和为 2+0+2+1+6+2+3 = 16，是一个完全平方数。所以 2021年06月23日也是一个完全日期。
# 请问，从 2023年1月1日到 2023年12月31日中，一共有多少个完全日期？
import datetime
def digit_sum(n):
    return sum(map(int,str(n)))

def is_perfect_date(year,month,day):
    date_sum = digit_sum(year) + digit_sum(month) + digit_sum(day)
    return int(date_sum ** 0.5)**2 == date_sum

start_date = datetime.datetime(2023,1,1)
end_date = datetime.datetime(2023,12,31)
count = 0
while start_date <= end_date:
    if is_perfect_date(start_date.year,start_date.month,start_date.day):
        count += 1
    start_date += datetime.timedelta(days=1)
print(f"从 2023年1月1日到 2023年12月31日中，一共有 {count} 个完全日期")