my_dict1 = {"王力宏":99,"ww":88,"周杰伦":77}
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1}，类型是：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2}，类型是：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3}，类型是：{type(my_dict3)}")

score1 = my_dict1["王力宏"]
print(score1)

my_dict4 = {
    "王力宏":{"语文":77,"数学":66,"英语":33},
    "周杰伦":{"语文":44,"数学":55,"英语":22},
    "林俊杰":{"语文":99,"数学":88,"英语":11}
}
print(my_dict4["王力宏"])
