import turtle

turtle.shape('turtle')


def circle(n=100, up=5):
    for i in range(n):
        turtle.forward(up)
        turtle.left(180 - 180 * (n - 2) / n)

    for i in range(n):
        turtle.forward(up)
        turtle.right(180 - 180 * (n-2) / n)


for j in range(3):
    circle()
    turtle.left(60)
