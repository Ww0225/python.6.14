# 小球从给定高度的地方自由落下，每次落地后反弹回原高度的52%，然后再落下，定义一函数ball_fun，
# 实现：计算小球在第n次落地时，所经过的路共多少米以及第n次反弹高度位置。
Cn = 0
Hn = 0
def ball_fun(high,n):
    global  Cn,Hn
    init_high = high
    for _ in range(n):
        Cn += init_high
        Hn = init_high * 0.52
        init_high = Hn
    Cn += Hn
    return Cn,Hn

if __name__ == '__main__':
    high = float(input("请输入小球原始落地高度:"))
    n = int(input("请输入小球落地的次数:"))
    sum_high,last_high = ball_fun(high,n)
    print(f"小球第{n}次落地时所经过的路:{sum_high}米")
    print(f"小球第{n}次落地时的反弹高度:{last_high}米")