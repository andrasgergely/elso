import turtle

def rajzol():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-75, 0)
    turtle.pendown()

    for _ in range(5):
        turtle.forward(100)
        turtle.left(72)

ablak = turtle.Screen()
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pensize(10)
turtle.pencolor("green")
turtle.listen()
turtle.onkey(rajzol, "h")
turtle.onkey(turtle.bye, "q")  #

turtle.mainloop()
