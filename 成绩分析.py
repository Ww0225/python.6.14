# 小蓝给学生们组织了一场考试，卷面总分为 100分，每个学生的得分都是一个0到100的整数
# 请计算这次考试的最高分、最低分和平均分
# 输入描述
# 输入的第一行包含一个整数(1n104)，表示考试人数接下来n行，每行包含一个0至100 的整数，表示一个学生的得分
# 输出描述
# 输出三行
# 第一行包含一个整数，表示最高分
# 第二行包含一个整数，表示最低分
# 第三行包含一个实数，四舍五入保留正好两位小数，表示平均分
exam_people = int(input())
score_list = [int(input()) for i in range(1,exam_people+1)]
print(max(score_list))
print(min(score_list))
print("{:.2f}".format(sum(score_list)/exam_people))