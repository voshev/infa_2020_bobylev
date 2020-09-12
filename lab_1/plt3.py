import numpy as np
import matplotlib.pyplot as plt


def func_for_graph(x):
    y = np.log((x * x + 1) * np.exp(-(np.abs(x) / 10)) / np.log(1 + np.tan(np.sin(x) * np.sin(x) + 1)))

    return y


x = np.arange(-10, 10.01, 0.01)
plt.plot(x, func_for_graph(x))
plt.grid(True)
plt.show()
