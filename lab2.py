import numpy as np
import matplotlib.pyplot as plt

#np.linalg.solve()
#np.vander(,increasing=True)

n = 100


def f(x):
    return 1/(1 + x**2)

x = np.linspace(-5, 5, n + 1)
vander = np.vander(x, increasing=True)

y = np.array([f(i) for i in x])
y = y[:, np.newaxis]

a = np.linalg.solve(vander,y)
p = vander.dot(a)

plt.plot(x,p)
plt.show()
