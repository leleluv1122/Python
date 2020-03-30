import turtle

turtle.pensize(3)

turtle.penup()
turtle.goto(-250, 60)
turtle.setheading(180)
turtle.pendown()
turtle.circle(40, steps = 3)

turtle.penup()
turtle.goto(-100, 0)
turtle.setheading(45)
turtle.pendown()
turtle.circle(40, steps = 4)

turtle.penup()
turtle.goto(30, 0)
turtle.setheading(36.5)
turtle.pendown()
turtle.circle(40, steps = 5)

turtle.penup()
turtle.goto(160, 0)
turtle.setheading(30)
turtle.pendown()
turtle.circle(40, steps = 6)

turtle.penup()
turtle.goto(290, 0)
turtle.pendown()
turtle.circle(40)

turtle.done()
