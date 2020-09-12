import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-3, 3.01, 0.01)
plt.plot(x, x*x - x - 6)
plt.grid(True)
plt.text(0, -3, r'x=3')
plt.text(0, 2, r'x=-2')
plt.show()
