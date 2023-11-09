import collections,random
money,red_num = map(int,input('请输入你要发的红包金额以及红包个数:').split())
if money < 0.1 or red_num < 2:
    print("红包金额或红包个数不正确，请重新设置发放")
else:
    red_dict = collections.defaultdict(float)
    for i in range(0,red_num):
        average_money = money/(red_num-i)
        max_money = average_money*(4/3)
        if i==0:
            red_money = round(random.uniform(average_money,max_money),2)
        elif 0<i<red_num-1:
            red_money = round(random.uniform(0.01, average_money * 2),2)
        else:
            red_money = round(money,2)
        red_dict[i + 1] = red_money
        money -= red_money
    for k,v in red_dict.items():
        print(f"用户{k} 抢到了 {v} 元")
    red_dict_sort = sorted(red_dict.items(),key=lambda x:x[1],reverse=True)
    print(f"最佳手气{red_dict_sort[0][0]},金额为:{red_dict_sort[0][1]}")