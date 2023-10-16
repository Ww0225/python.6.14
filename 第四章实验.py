# import datetime
# sum = datetime.date.today().timetuple().tm_yday
# print(f"今天是今年的第{sum}天")

import random
ball = [[random.randint(1,34) for i in range(6)],[random.randint(1,17)]]
print(f"生成的红色球为：{ball[0]}\n蓝色球为：{ball[1]}")