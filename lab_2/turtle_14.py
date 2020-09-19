import turtle

turtle.shape('turtle')


def star(n, a=50):
    for i in range(n):
        turtle.forward(a)
        turtle.left(180*(n-1)/n)


star(5, 100)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

star(11, 150)