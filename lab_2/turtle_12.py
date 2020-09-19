import turtle

turtle.shape('turtle')


def part_of_circle(n=100, up=5):
    i = 0
    while i < n / 2:
        turtle.forward(up)
        turtle.right(180 - 180 * (n - 2) / n)
        i += 1


turtle.left(90)
part_of_circle()
for j in range(4):
    part_of_circle(100, 1)
    part_of_circle()