import turtle

a = 90
n = 12

turtle.shape('turtle')
for i in range(n):
    turtle.forward(a)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(a)
    turtle.left(180 - 360 / n)
