from collections import OrderedDict
stu_dict ={"张三":"2002-12-04","李四":"2001-03-15","王五":"2003-05-17",
    "何洋":"2002-07-30","李诗":"2001-09-10","谢明":"2003-10-18"}
sorted_dict = OrderedDict(sorted(stu_dict.items(),key=lambda x:x[1]))
print("学生信息原始顺序如下:")
for k,v in stu_dict.items():
    print(f"{k} : {v}")
print("按照出生日期升序后的结果如下:")
for k,v in sorted_dict.items():
    print(f"{k} : {v}")
search_name = input("请输入你要查询的学生名字：")
print(sorted_dict.get(search_name,"你查找的学生不存在"))