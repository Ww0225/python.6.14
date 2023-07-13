my_set = {"ww","python","ww","python","ww","python"}
my_set_empty = set()
print(f"my_set得内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty得内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

my_set.add("java")
print(my_set)
my_set.remove("java")
print(my_set)

print(my_set.pop())

my_set.clear()
print(my_set)