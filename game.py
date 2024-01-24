import turtle
screen = turtle. Screen()
screen.bycolor("Black")
pen = turtle.Turtle()
pen.speed(2)
pen.width(2)
colors = ['red''orange' 'blue' ]
for i in range(360):
    pen.pencolor(colors[i%6])
    pen.forward(i)
    pen.right(50)
    turtle.done()