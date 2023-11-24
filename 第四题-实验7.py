# 编写Python代码，模拟决赛现场最终成绩的计算过程。
# 要求包含：
# (1)输入评委总人数在3人（包含）以上;
# (2)每个评委分数须0-10之间;
# (3)去掉最高分与最低分;
# (4)对输入的人数、分数利用异常进行处理。
# 操作方法与步骤：创建Test4.py程序，使用 while输入数，并对人数进行判断，再输入打分，
# 判断打分是否为0-100的数字，整个过程都需要使用try.....except进行处理

class InvalidInputError(Exception):
    pass

def calculate_score(scores):
    sorted_scores = sorted(scores)
    trimmed_scores = sorted_scores[1:-1]
    final_score = sum(trimmed_scores) / len(trimmed_scores)
    print(f"最终成绩为: {final_score:.2f}")

scores = []
while True:
    try:
        judge_people = int(input("请输入评委总人数:"))
        if judge_people < 3:
            raise InvalidInputError("评委人数不能少于3人")
        for i in range(judge_people):
            score = float(input(f"请第{i+1}位评委打分（0-10分）:"))
            if score < 0 or score > 10:
                raise ValueError
            scores.append(score)
        calculate_score(scores)
        break
    except InvalidInputError as e:
        print(e)
        scores = []
    except ValueError:
        print("输入评分错误，请重新输入（0-10）")
        scores = []
