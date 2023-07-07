t1 = (1,"Hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

t4 = ("hello")
print(f"t4的类型是：{type(t4)},内容是：{t4}")

t5 = ("hello",)
print(f"t5的类型是：{type(t5)},内容是：{t5}")

t6 = ((1,2,3),(4,5,6))
t4 = ("hello")
print(f"t6的类型是：{type(t6)},内容是：{t6}")

print(t6[1][2])

t7 = ("传承教育","黑马程序员","Python","Python")
index = t7.index("Python")
print(index)
print(t7.count("Python"))
print(len(t7))

index = 0
while index < len(t7):
    print(t7[index])
    index += 1

for index in t7:
    print(index)

t9 = (1,2,["ww","python"])
print(t9)
t9[2][1] = "java"
print(t9)
