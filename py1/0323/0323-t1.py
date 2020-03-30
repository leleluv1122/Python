import turtle

x1, y1 = eval(input("x1, y1 input: "))
x2, y2 = eval(input("x2, y2 input: "))
tx = (x1 + x2)/2
ty = (y1 + y2)/2
d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

turtle.showturtle()

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")

turtle.goto(x2, y2)

turtle.write("Point 2")

turtle.penup()
turtle.goto(tx, ty)
turtle.pendown()
turtle.write(d)

turtle.done()