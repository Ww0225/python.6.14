# 1、编写程序：一盘棋一共64个格子，在第一个格子放1粒米，
# 第二个格子里放2粒米，第三个格子里放4粒米，第四个格子里放8粒米，
# 以此类推，后面每个格子里的米都是前一个格子里的2倍，一直把64个格子都放满。
# 一共需要多少粒米呢？使用推导式计算并输出。
rice_list = [2**i for i in range(64)]
print(sum(rice_list))