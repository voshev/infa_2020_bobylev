import turtle
import numpy as np

cycles_number = 1000
angles_number = 100
R = 0.05
delta_R = 0.01
i = 1
turtle.shape('turtle')
for i in range(cycles_number):
    turtle.forward(2 * R * np.cos(np.pi / angles_number))
    turtle.left(360 / angles_number)
    turtle.left(360 / angles_number)
    R += delta_R
    i += 1
