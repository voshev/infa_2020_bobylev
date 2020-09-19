import turtle

turtle.shape('turtle')
n = 100
up = 10
for i in range(n):
    turtle.forward(up)
    turtle.left(180 - 180 * (n - 2) / n)
