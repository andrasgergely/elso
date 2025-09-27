import turtle

def rajzol():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)

ablak = turtle.Screen()
turtle.hideturtle()
turtle.bgcolor("grey")
turtle.pensize(10)
turtle.pencolor("white")
turtle.listen()
turtle.onkey(rajzol, "h")
turtle.onkey(turtle.bye, "q")

turtle.mainloop()
