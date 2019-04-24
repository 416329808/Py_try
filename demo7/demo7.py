import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(0, 2*np.pi, 500)
y1 = 2*x + 1
y2 = x**2
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='$y=2*x+1$', color='red', linewidth=2)
plt.plot(x, y2, 'b--', label='$y=x**2$', color='black', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('2*x+1 and x**2')
plt.legend()
plt.show()



