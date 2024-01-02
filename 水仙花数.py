# 自幂数是指一个n(3或4)位数，它的每个位上的数字的 n 次幂之和等于它本身。
# 例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数，3位数的自幂数被称为水仙花数。
# 当n为4时，有1^4 + 6^4 + 3^4 + 4^4 = 1634，1634即是n为4时的一个自幂数，4位数的自幂数被称为玖瑰花数。
# 程序运行时，输入数字3或4，选择求解水仙花数或玖瑰花数，结果放置在列表中按照从小到大顺序输出。如下图所示。
def water_flower():
    water_flower_list = [n for n in range(10**2,10**3) if sum(map(lambda x:int(x)**3,str(n))) == n]
    return water_flower_list
print(water_flower())