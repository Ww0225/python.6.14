from collections import defaultdict
initial_ability = 1
study_up = 0.08
relax_down = 0.05
term = 16           # 一学期16周
print("请输入你本周表现情况，0代表放松，1代表努力：")
week_list = [int(input()) for i in range(7)]
week_study_day = week_list.count(1)
week_relax_day = week_list.count(0)
print(f"本周你努力了{week_study_day}天")
print(f"本周你放松了{week_relax_day}天")
ability_value = defaultdict(float)
for week in range(1,term+1):
    ability_value[week] = (initial_ability+0.01)**(week_study_day*week)\
                          *(initial_ability-0.01)**(week_relax_day*week)
print(f"你本周的能力表现值为：{ability_value[1]}")
print(f"以此坚持一学期，16周后你的能力表现值为：{ability_value[term]}")