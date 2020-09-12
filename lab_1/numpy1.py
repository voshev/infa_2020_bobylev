import numpy as np


def new_log(x):
    a = 1 / (np.exp(np.sin(x)) + 1)
    b = 5 / 4 + 1 / (x ** 15)
    y = np.log(a / b) / np.log(1 + x ^ 2)
    return y


print('y(1) = ', new_log(1))
print('y(10) = ', new_log(10))
print('y(1000) = ', new_log(1000))
