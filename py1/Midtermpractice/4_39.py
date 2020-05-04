import turtle
import math

x1, y1 = eval(input("Enter the venter of a circle x, y: "))
radius1 = eval(input("Enter the radius of the circle: "))
x2, y2 = eval(input("Enter the venter of a circle2 x, y: "))
radius2 = eval(input("Enter the radius of the circle2: "))

# Draw the circle
turtle.penup()
turtle.goto(x1, y1-radius1)
turtle.pendown()
turtle.circle(radius1)

# Draw the circle
turtle.penup()
turtle.goto(x2, y2-radius2)
turtle.pendown()
turtle.circle(radius2)

l = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

turtle.penup()
turtle.setheading(270)
turtle.forward(50)

if l >= (radius1+radius2):
    turtle.write("원2와 원1은 겹치지 않습니다.")
elif radius2-radius1 > l:
    turtle.write("원2는 원1의 내부에 있습니당!!")
elif l <= (radius1+radius2):
    turtle.write("원2는 원1과 겹칩니다.")


turtle.hideturtle()
turtle.done()