# 从1921年到2021年，中国共产党走过了整整一百年的历程。
# 2021年是中国共产党成立100周年的日子，7月1 日在北京天安门广场举行了盛大的庆典活动，
# 中国共产党带领了中国走向繁荣富强，我为自己是中国人而感到骄傲、自豪。
# 请同学们使用Python标库中的turtle库绘制中国共产党党徽，用于庆祝中国共产党成立100周年
import turtle
def draw_rectangle():
    # 绘制红色矩形背景
    turtle.color("red")
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(-300, 300)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(630)
        turtle.right(90)
        turtle.forward(500)
        turtle.right(90)
    turtle.end_fill()

def draw_hammer():
    # 绘制锤头
    turtle.color("yellow", "yellow")
    turtle.penup()
    turtle.goto(10, 220)
    turtle.seth(225)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fd(125)
    turtle.right(90)
    turtle.fd(50)
    turtle.right(90)
    turtle.fd(100)
    turtle.right(90)
    turtle.circle(25,90)
    turtle.end_fill()
    # 绘制锤头柄
    turtle.penup()
    turtle.goto(-40, 190)
    turtle.seth(-45)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()

def draw_sickle():
    # 绘制月牙型镰刀
    turtle.color("yellow", "yellow")
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.seth(-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100,180)
    turtle.fd(20)
    turtle.right(157)
    turtle.circle(-115,190)
    turtle.left(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(20)
    turtle.left(80)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(20)
    turtle.end_fill()
    # 绘制镰刀圆柄
    turtle.up()
    turtle.goto(-90, 20)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

def write_text():
    # 隐藏海龟，设置画笔，移动画笔并写入文字
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-300, -150)
    turtle.color("yellow")
    turtle.write("热烈庆祝中国共产党成立一百周年！", font=("华文行楷", 30, ''))

if __name__ == '__main__':
    turtle.speed(5)
    draw_rectangle()
    draw_hammer()
    draw_sickle()
    write_text()
    turtle.done()