import turtle
import numpy as np

turtle.shape('turtle')


def rectangle(n):
    for i in range(n):
        length = R * 2 * (np.cos(np.pi * (n-2) / 2 / n))
        turtle.forward(length)
        turtle.left(360 / n)


rectangle_num = 10
R = 50
delta_R = 30
for j in range(3, rectangle_num):
    turtle.left(90 * (j + 2) / j)
    rectangle(j)
    turtle.right(90 * (j + 2) / j)
    turtle.penup()
    turtle.forward(delta_R)
    turtle.pendown()
    R += delta_R
