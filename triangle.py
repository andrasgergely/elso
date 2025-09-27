import turtle

def rajzol() :
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-75, 0)
    turtle.pendown()
    turtle.pendown()
    #turtle.right(30)
    for _ in range(3):
        turtle.forward(150)
        turtle.left(120)

ablak = turtle.Screen()
turtle.hideturtle()
turtle.bgcolor("green")
turtle.pensize(10)
turtle.pencolor("blue")
turtle.listen()
turtle.onkey(rajzol, "h")
turtle.onkey(turtle.bye,"q")

turtle.mainloop()

