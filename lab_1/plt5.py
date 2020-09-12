import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([0.99, 0.49, 0.35, 0.253, 0.18])

plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()

p_1 = np.polyfit(x, y, 1)
p_1_f = np.poly1d(p_1)
plt.plot(x, p_1_f(x))


p_2 = np.polyfit(x, y, 2)
p_2_f = np.poly1d(p_2)
plt.plot(x, p_2_f(x))


plt.show()