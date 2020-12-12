import turtle
from random import *

turtle.shape('turtle')
turtle.speed(10)
while True:
    turtle.forward(100 * random())
    turtle.right(360 * random())
