import turtle
r = 100
x,y = 0,-100
colors = ['Purple','Green','Gold','Red','Blue']
for n in range(5):
    turtle.fillcolor(colors[n])
    turtle.begin_fill()
    turtle.up()
    turtle.goto(x,y)
    turtle.pd()
    turtle.circle(r)
    r -= 20
    y += 20
    turtle.end_fill()
turtle.ht()
turtle.done()