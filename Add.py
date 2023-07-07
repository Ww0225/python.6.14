def add(x,y):
    """
    
    :param x:
    :param y:
    :return:
    """
    return x+y

r = add(1,2)
print(r)

def say_hi():
    print("hi")

result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")
