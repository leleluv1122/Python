import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-250, 60)
turtle.setheading(180)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(-100, 0)
turtle.setheading(45)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(40, steps = 4) # Draw a square
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(30, 0)
turtle.setheading(36.5)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.circle(40, steps = 5) # Draw a pentagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(160, 0)
turtle.setheading(30)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(40, steps = 6) # Draw a hexagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(290, 0)
turtle.pendown()
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(40)  # Draw a circle
turtle.end_fill()  # Fill the shape

turtle.color("green")
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

turtle.color("black")
turtle.write("Cool Colorful Shapes",
    font = ("Times", 18, "bold"))
turtle.hideturtle() # 깔 끔 쓰 ~ 화살표 XX

turtle.done()