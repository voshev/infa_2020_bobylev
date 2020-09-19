import turtle

a = 10
delta_a = 10
n = 10

turtle.shape('turtle')
for i in range(n):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    a += delta_a
