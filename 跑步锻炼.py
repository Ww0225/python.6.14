# 小蓝每天都锻炼身体。
# 正常情况下，小蓝每天跑1千米。如果某天是周一或者月初(1日)，
# 为了激励自己，小蓝要跑2千米。如果同时是周一或月初，小蓝也是跑2千米。
# 小蓝跑步已经坚持了很长时间，从2000年1月1日周六（含）到
# 2020年10月1日周四（含）。请问这段时间小蓝总共跑步多少千米？
import datetime

start = datetime.date(2000,1,1)
end = datetime.date(2020,10,1)
ans = 0
while end >= start:
    if start.day == 1 or start.weekday() == 0:
        ans += 2
    else:
        ans += 1
    start += datetime.timedelta(days=1)
print(ans)
