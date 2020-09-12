import numpy as np
import random
import matplotlib.pyplot as plt

numbers_3 = []
for i in range(1, 1000, 2):
    numbers_3.append(i)

a = random.choice(numbers_3)
b = random.random()

x = np.arange(-5, 5.01, 0.01)
y = np.cos((np.pi * x))
i = 0
while i < 100:
    y = y + (b ** i) * np.cos((a ** i) * np.pi * x)
    i = i + 1
plt.plot(x, y)
plt.grid()
plt.show()
