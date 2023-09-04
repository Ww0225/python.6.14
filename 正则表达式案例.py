import re

r = '^[0-9a-zA-Z]{6,10}$'
s = '12345610'
print(re.findall(r,s))

r1 = '^[1-9][0-9]{4,10}$'
s1 = '123456'
print(re.findall(r1,s1))

r2 = '^[\w-]+(\.[\w-]+)*@(qq|163|email)(\.[\w-]+)+$'
s2 ='156112@qq.com'
print(re.findall(r2,s2))