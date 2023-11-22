try:
    name = input("输入名字（2-5位）:")
    if len(name)<2:
        raise ValueError
    if len(name)>5:
        raise ValueError("名字大于5位")
    else:
        print("你输入的名字是：",name)
except ValueError as e:
    print(e)