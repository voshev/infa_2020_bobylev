import turtle

k = 10  # number of squares
a = 20  # length
delta_a = 10  # space
turtle.shape('turtle')

for i in range(k):
    for j in range(4):
        turtle.pendown()
        turtle.forward(a)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(delta_a)
    turtle.right(90)
    turtle.forward(delta_a)
    turtle.left(180)
    a += 2 * delta_a
