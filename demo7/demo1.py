import turtle
turtle.pensize(1)
turtle.pencolor("white")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.hideturtle()
while True:
    turtle.forward(200)
    turtle.right(144)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.mainloop()
