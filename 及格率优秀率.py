import os
import sys

# 请在此输入您的代码
n = int(input())
jigelv = 0
youxiulv = 0
for i in range(n):
  score = int(input())
  if score>=85:
    youxiulv = youxiulv+1
    jigelv = jigelv +1
  elif score>=60:
    jigelv = jigelv + 1
print("{:.0f}%".format(100*jigelv/n))
print("{:.0f}%".format(100*youxiulv/n))