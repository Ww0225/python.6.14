import jieba.analyse
file = open('红楼梦.txt',encoding='utf-8')
str = file.read()
rs1 = jieba.analyse.extract_tags(str,10,False,('nr',))
print(rs1)
print('--------------------------------------------------------------------')
rs2 = jieba.analyse.extract_tags(str,10,True,('nr',))
for name,weight in rs2:
    print(f"{name} \t {weight}")