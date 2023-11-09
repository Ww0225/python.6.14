pm_num = float(input("请输入PM2.5的值："))
if pm_num<= 35:
    print(f"{pm_num}对应的空气质量为: 以下优")
elif pm_num > 35 and pm_num < 75:
    print(f"{pm_num}对应的空气质量为: 良")
elif pm_num > 75 and pm_num <= 115:
    print(f"{pm_num}对应的空气质量为: 轻度污染")
elif pm_num > 115 and pm_num <= 150:
    print(f"{pm_num}对应的空气质量为: 中度污染")
elif pm_num > 150 and pm_num <= 250:
    print(f"{pm_num}对应的空气质量为: 重度污染")
elif pm_num > 250:
    print(f"{pm_num}对应的空气质量为: 严重污染")