# -*- coding: utf-8 -*-
# 使用csv模块读取并输出“iris.csv”文件中的内容，
# 并将“sepal_length”长度为6以上的存入iris1_1.csv中。
import csv
with open('iris.csv','r',encoding='gbk') as in_file:
    reader = csv.DictReader(in_file)
    words = [row for row in reader if eval(row['sepal_length']) >= 6]
with open('iris1_1.csv','w',encoding='gbk',newline='') as out_file:
    writer = csv.DictWriter(out_file,fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(words)