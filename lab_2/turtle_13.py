import turtle

turtle.shape('turtle')


def circle(n=100, up=5):
    for i in range(n):
        turtle.forward(up)
        turtle.left(180 - 180 * (n - 2) / n)


def part_of_circle(n=100, up=5):
    i = 0
    while i < n / 2:
        turtle.forward(up)
        turtle.left(180 - 180 * (n - 2) / n)
        i += 1

# the head
turtle.begin_fill()
circle()
turtle.color('yellow')
turtle.end_fill()
turtle.color('black')


# the eyes
turtle.penup()
turtle.goto(-50, 90)
turtle.pendown()

turtle.begin_fill()
circle(100, 1)
turtle.color('blue')
turtle.end_fill()
turtle.color('black')

turtle.penup()
turtle.goto(50, 90)
turtle.pendown()

turtle.begin_fill()
circle(100, 1)
turtle.color('blue')
turtle.end_fill()
turtle.color('black')


# the mouth
turtle.penup()
turtle.goto(-30, 40)
turtle.pendown()


turtle.color('red')
turtle.width(5)
turtle.right(90)
part_of_circle(40, 5)
turtle.color('black')


# the nose
turtle.penup()
turtle.goto(0, 90)
turtle.pendown()

turtle.color('black')
turtle.width(5)
turtle.backward(40)
