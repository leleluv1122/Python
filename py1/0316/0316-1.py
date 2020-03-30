import turtle

# turtle을 불러온다
turtle.showturtle()
turtle.write("Welcome to Python")

#앞으로 100pixel만큼 간다
turtle.forward(100)

# 90도 오른쪽으로 돌리고
turtle.right(90)

# red 색으로 50만큼
turtle.color("red")
turtle.forward(50)

turtle.right(90)
turtle.color("green")
turtle.forward(100)

turtle.right(45)
turtle.forward(80)

#끝내기
turtle.done()