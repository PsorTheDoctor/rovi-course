import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x**3 - x**2 + 2

def derivFunc(x):
    return 3 * x**2 - 2 * x

def newtonRhapson(x):
    h = func(x) / derivFunc(x)
    i = 0
    while abs(h) >= 0.0001:
        h = func(x) / derivFunc(x)
        x -= h
        i += 1
        print(f'Step {i}: x = {h}')

    print('The value of the root is: %.4f'% x)


xs = np.arange(-20, 20, 1)
plt.plot(func(xs), label='function')
plt.plot(derivFunc(xs), label='derivative')
plt.legend()
plt.show()

x0 = -20  # Initial guess
newtonRhapsod(x0)
