import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('black')


square = turtle.Turtle()
square.shape('square')
square.color('light green')
square.speed('slowest')
square.up()


for i in range(4):
    square.sety(160 + i * 20)
    square.stamp()

for i in range(4):
    square.goto(i*20, 220)
    square.stamp()
square.goto(60, 200)
square.stamp()


square.goto(0, 140)
square.shape('square')
square.color('orange')
square.speed('fastest')


for k in range(30):
    for i in range(5+k):
        square.goto(i*6, 140-k*3)
        square.stamp()
        square.goto(i*-6, 140-k*3)
        square.stamp()


circle = turtle.Turtle()
circle.shape('circle')
circle.color('orange')
circle.speed('fastest')
circle.up()


circle.goto(210, 50)
circle.stamp()
circle.goto(-210, 50)
circle.stamp()


l = 0
for k in range(29, -1, -1):
    for i in range(5+k, -1, -1):
        square.goto(i*6, 50-l*3)
        square.stamp()
        square.goto(i*-6, 50-l*3)
        square.stamp()
    l += 1


triangle = turtle.Turtle()
triangle.shape('triangle')
triangle.color('white')
triangle.speed('slowest')
triangle.shapesize(1)
triangle.left(90)
triangle.up()


for i in range(3):
    triangle.goto(-60 + i*60, 20)
    triangle.stamp()
triangle.right(180)
triangle.goto(-30, 40)
triangle.stamp()
triangle.goto(30, 40)
triangle.stamp()


circle.shape('circle')
circle.color('purple')
circle.speed('slowest')
circle.shapesize(2)


circle.goto(-80, 60)
circle.stamp()
circle.goto(80, 60)
circle.stamp()


turtle.exitonclick()