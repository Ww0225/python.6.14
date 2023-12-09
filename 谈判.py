# 在很久很久以前，有个部落居住在平原上，依次编号为1到。第
# i个部落的人数为t;。
# 有一年发生了灾荒。年轻的政治家小蓝想要说服所有部落一同应对灾
# 荒，他能通过谈判来说服部落进行联合。
# 每次谈判，小蓝只能邀请两个部落参加，花费的金币数量为两个部落
# 的人数之和，谈判的效果是两个部落联合成一个部落（人数为原来两
# 个部落的人数之和)。
# 输入描述
# 输入的第一行包含一个整数，表示部落的数量。
# 第二行包，含个正整数，依次表示每个部落的人数。
# 其中，1≤n≤1000,1≤t;≤104。
# 输出描述
# 输出一个整数，表示最小花费。
n = int(input())
people = list(map(int,input().split()))
people.sort()
cost = 0
while len(people) > 1:
    merge_cost = people[0] + people[1]
    cost += merge_cost
    people.append(merge_cost)
    people = people[2:]
    people.sort()
print(cost)