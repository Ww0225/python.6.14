# 问题描述
# 对于一个日期，我们可以计算出年份的各个数位上的数字之和，也可以
# 分别计算月和日的各位数字之和。请问从1900年1月1日至9999年
# 12月31日，总共有多少天，年份的数位数字之和等于月的数位数字之
# 和加日的数位数字之和。
# 例如，2022年11月13日满足要求，因为2+0+2+2=(1+
# 1)+(1+3)。
# 请提交满足条件的日期的总数量。

from datetime import *

start = datetime(1900,1,1)
end = datetime(9999,12,31)
count = 0
while start < end:
      year = int(start.year)
      month = int(start.month)
      day = int(start.day)
      if (year // 1000 + (year // 100 % 10) + (year // 10 % 10) + (year % 10)) == (month // 10 + month % 10 + day // 10 + day % 10):
        count += 1
      start += timedelta(days=1)
print(count)