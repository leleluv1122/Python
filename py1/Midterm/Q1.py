import turtle

x1, y1 = eval(input("rect1의 중심좌표 x y 입력: "))
w1, h1 = eval(input("rect1 폭, 높이 입력: "))
x2, y2 = eval(input("rect2의 중심좌표 x y 입력: "))
w2, h2 = eval(input("rect2 폭, 높이 입력: "))

left1 = x1 - w1/2
right1 = x1 + w1/2
top1 = y1 + h1/2
bottom1 = y1 - h1/2

left2 = x2 - w2/2
right2 = x2 + w2/2
top2 = y2 + h2/2
bottom2 = y2 - h2/2


turtle.penup()
turtle.goto(x1-w1/2, y1-h1/2)
turtle.pendown()
turtle.forward(w1)
turtle.setheading(90)
turtle.forward(h1)
turtle.setheading(180)
turtle.forward(w1)
turtle.setheading(270)
turtle.forward(h1)


turtle.penup()
turtle.goto(x2-w2/2, y2-h2/2)
turtle.pendown()
turtle.setheading(0)
turtle.forward(w2)
turtle.setheading(90)
turtle.forward(h2)
turtle.setheading(180)
turtle.forward(w2)
turtle.setheading(270)
turtle.forward(h2)

turtle.hideturtle()


turtle.penup()
turtle.setheading(270)
turtle.forward(100)

if left1 < left2 and right1 > right2 and top1 > top2 and bottom1 < bottom2:
    turtle.write("두 번째 사각형이 첫 번째 사각형의 내부에 있다")
elif right1 < left2 or left1 > right2:
    turtle.write("두 번째 사각형이 첫 번째 사각형의 외부에 있다.")
elif (right1 > right2 or left1 < left2) and (top1 < bottom2 or bottom1 > top2):
    turtle.write("두 번째 사각형이 첫 번째 사각형의 외부에 있다.")
else:
    turtle.write("두 번째 사각형과 첫 번째 사각형은 겹친다")

turtle.done()