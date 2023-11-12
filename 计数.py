# 输入一个十进制整数，统计期中每个基数出现的次数，并按出现频次由高到低输出。
# 如：
# 输入:  673313426236
# 输出:  3 4
#      6 3
#      2 2
#      7 1
#      4 1
#      1 1
num = int(input(""))

def frequencyOfDigits(number):
    #请在两行注释之间的位置完成函数定义
    ###############################################
    num_dict = {}
    for i in str(number):
        num_dict[i] = num_dict.get(i,0)+1
    sort_dict = dict(sorted(num_dict.items(),key=lambda x:x[1],reverse=True))
    for k,v in sort_dict.items():
        print(f"{k} {v}")
    ###############################################


frequencyOfDigits(num)