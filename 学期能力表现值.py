# 2、天天向上的力量----毛泽东主席于1951年题词“好好学习，天天向上！”，成为激励一代又一代中国人奋发图强的经典语录。
# 那么，“好好学习”最终能够达到怎样的学习效果？
# 假设学习者的初始能力值基数记为1，每周努力学习1天，能力值上升8%；躺平对待1天，能力值下降5%。
# 利用Python的defaultdict类实现计算学生一个学期（20周）的能力表现值。20周的能力表现值计算，
# 可以通过按周来计算，即（1）先统计每周表现的情况，
# 计算公式：（（1+0.08）**一周努力天数×（1-0.05）**一周躺平天数），其中**代表求幂.
# （2）再对20周所有表现值求和（22.30为合格）。
# 操作方法与步骤：通过以上几点提示：
# （1）可以先使用random模块的choice函数生成一个列表，列表中包含20个子列表，每个子列是其中一周表现情况（随机生成）
# （2）定义一个包含默认值的空字典dict1和一个存放能力表现值的列表term_count，然后对（1）步生成的列表数据按周（遍历）统计努力与躺平的天数，统计结果存入字典dict1，同时调用上述公式计算一周能力表现值，能力表现值存入term_count。
# （3）将term_count中的能力表现值求和，得到总表现值。
import random
from collections import defaultdict
term_study_or_relax = [[random.choice([0,1])for _ in range(7)]for _ in range(20)]
term_count = 0
term = 1
for week in term_study_or_relax:
    week_dict = defaultdict(int,{day:week.count(day) for day in week})
    week_ability = (1+0.08)**week_dict[0]*(1-0.05)**week_dict[1]
    print(f"第 {term} 周，努力天数：{week_dict[0]}，躺平天数：{week_dict[1]}，表现值：{week_ability}")
    term += 1
    term_count += week_ability
print(f"这学期的能力表现值：{term_count}")