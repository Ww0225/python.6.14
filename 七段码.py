# 上图给出了七段码数码管的一个图示，数码管中一共有7段可以发光
# 的二极管，分别标记为a,b,c,d,e,f,g。
# 小蓝要选择一部分二极管（至少要有一个）发光来表达字符。在设计
# 字符的表达时，要求所有发光的二极管是连成一片的。
# 例如：b发光，其他二极管不发光可以用来表达一种字符。
# 例如℃发光，其他二极管不发光可以用来表达一种字符。这种方案与
# 上一行的方案可以用来表示不同的字符，尽管看上去比较相似。
# 例如：a,b,c,d,e发光，f,g不发光可以用来表达一种字符。
# 例如：b,f发光，其他二极管不发光则不能用来表达一种字符，因为
# 发光的二极管没有连成一片。
# 请问，小蓝可以用七段码数码管表达多少种不同的字符？
import itertools
data = {
  'a':['f','b'],
  'b':['a','g','c'],
  'c':['b','g','d'],
  'd':['e','c'],
  'e':['d','g','f'],
  'f':['a','g','e'],
  'g':['f','b','e','c']
}

ans = []
str = 'abcdefg'
count = 0
for i in range(7):
  for x in itertools.combinations(str,i):
    ans.append(''.join(x))
for s1 in ans:
  if len(s1) == 1:
    count += 1
    continue
  for situation in itertools.permutations(s1):
    for c in range(1,len(situation)):
      if situation[c-1] not in data[situation[c]]:
        break
    else:
      count+=1
      break
print(count)
