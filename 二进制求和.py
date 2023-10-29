# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和
a,b = map(str,input().split())
print(bin(int(a,2)+int(b,2))[2:])