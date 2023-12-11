import turtle
def draw_rectangle(x,y,width,height):
    turtle.up()
    turtle.goto(x,y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_star(x,y,big=True,pos=0,radius=50):
    turtle.fillcolor('yellow')
    turtle.pencolor('yellow')
    turtle.up()
    turtle.goto(x,y)
    if not big:
        turtle.setheading(pos)
    turtle.down()
    turtle.begin_fill()
    for x in range(5):
        turtle.forward(radius)
        turtle.right(144)
    turtle.end_fill()

if __name__ == '__main__':
    x,y = -200,-100
    width,height = 438,292
    draw_rectangle(x,y,width,height)
    turtle.speed(3)
    draw_star(-170, 145)
    draw_star(-100, 180, False, 260, 20)
    draw_star(-85, 145, False, 30, 20)
    draw_star(-85, 120, False, 3, 20)
    draw_star(-100, 100, False, 250, 20)
    turtle.hideturtle()
    turtle.mainloop()