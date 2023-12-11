# 使用turtle乌龟绘制奥运五环
import turtle
def draw_circle(x,y,color,r=45):
    turtle.pencolor(color)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(r)

if __name__ == '__main__':
    colors = ['blue','black','red','yellow','green']
    xy_list = [(-110, -25), (0, -25), (110, -25), (-55, -75), (55, -75)]
    scwide = 400
    scheight = 400
    turtle.pensize(5)
    turtle.speed(6)
    turtle.screensize(scwide, scheight)
    for n in range(5):
        draw_circle(xy_list[n][0],xy_list[n][1],colors[n])
    turtle.hideturtle()
    turtle.done()
