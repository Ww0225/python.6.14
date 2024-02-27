# 题目描述
# 2020年春节期间，有一个特殊的日期起了大家的注意：2020年2
# 月2日。因为如果将这个日期按“yyyymmdd”的格式写成一个8位数
# 是20200202，恰好是一个回文数。我们称这样的日期是回文日期。
# 有人表示20200202是“千年一遇”的特殊日子。对此小明很不认同，
# 因为不到2年之后就是下一个回文日期：20211202即2021年12月2日。
# 也有人表示20200202并不仅仅是一个回文日期，还是一个
# ABABBABA型的回文日期。对此小明也不认同，因为大约100年后
# 就能遇到下一个ABABBABA型的回文日期：21211212即2121年12
# 月12日。算不上“千年一遇”，顶多算“千年两遇”。
# 给定一个8位数的日期，请你计算该日期之后下一个回文日期和下一
# 个ABABBABA型的回文日期各是哪一天。
# 输入描述
# 输入包含一个八位整数N,表示日期。
# 对于所有评测用例，10000101≤N≤89991231，保证N是一个合法日期的8位数表示。
# 输出描述
# 输出两行，每行1个八位数。第一行表示下一个回文日期，第二行表
# 示下一个ABABBABA型的▣文日期。
import datetime
n = input()
year = int(n[0:4])
month = int(n[4:6])
day = int(n[6:])
date = datetime.date(year,month,day)
flag = True
while True:
    date += datetime.timedelta(days=1)
    strdate = str(date).replace('-', '')
    if strdate == strdate[::-1]:
        if flag:
            print(strdate)
            flag = False
        if strdate[0] == strdate[2] == strdate[5] == strdate[7] and strdate[1] == strdate[3] == strdate[4] == strdate[6]:
            print(strdate)
            break
