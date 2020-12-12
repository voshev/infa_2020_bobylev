from random import randint
import turtle

number_of_turtles = 20
steps_of_time_number = 10000

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shape("circle")
    unit.pensize(1)
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(-180, 180))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(5)
        a, b = unit.pos()
        if b < -200:
            unit.left((360 - unit.heading()) * 2)
        if b > 200:
            unit.right((unit.heading()) * 2)
        if a < -200:
            unit.right((unit.heading() - 90) * 2)
        if a > 200:
            unit.left((90 - unit.heading()) * 2)
