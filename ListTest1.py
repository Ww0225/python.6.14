my_list = ["ww","it","python"]
value = my_list.index("ww")
print(value)
print(my_list[value])

my_list[1] = "hello"
print(my_list[1])

my_list.insert(1,"888")
print(my_list)

my_list.append("study")
print(my_list)

my_list = [1,2,3]
my_list.extend([4,5,6])
print(my_list)

my_list = ["ww","it","python"]
del my_list[1]
print(my_list)
pop = my_list.pop(1)
print(pop)
print(my_list)

my_list = [1,2,3,2,3]
my_list.remove(2)
print(my_list)

my_list.clear()
print(my_list)

my_list = [1,2,3,2,3]
count = my_list.count(2)
print(count)
len = len(my_list)
print(len)