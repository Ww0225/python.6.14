import csv
with open("C:\\Users\Administrator\Desktop\某地区房屋销售数据.csv",mode='r',encoding='gbk') as file:
    csvfile = csv.DictReader(file)
    for i in csvfile:
        print(i)