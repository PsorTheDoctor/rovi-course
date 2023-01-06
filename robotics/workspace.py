import numpy as np
import matplotlib.pyplot as plt

# 2-link scara mechanism
l1 = 1
l2 = 1.5
nSamples = 100
theta1 = np.linspace(0, 210, nSamples) * np.pi / 180
theta2 = np.linspace(0, 180, nSamples) * np.pi / 180
th1, th2 = np.meshgrid(theta1, theta2, indexing='ij')
x = l1 * np.cos(th1) + l2 * np.cos(th1 + th2)
y = l1 * np.sin(th1) + l2 * np.sin(th1 + th2)

plt.figure(1)
plt.plot(x, y, 'b.')
plt.xlabel('x')
plt.ylabel('y')

# 3-link mechanism
l1 = 1
l2 = 1.5
l3 = 1.25
nSamples = 10
theta1 = np.linspace(-45, 130, nSamples) * np.pi / 180
theta2 = np.linspace(0, 90, nSamples) * np.pi / 180
theta3 = np.linspace(0, 80, nSamples) * np.pi / 180
th1, th2, th3 = np.meshgrid(theta1, theta2, theta3, indexing='ij')
x = l1 * np.cos(th1) + l2 * np.cos(th1 + th2) + l3 * np.cos(th1 + th2 + th3)
y = l1 * np.sin(th1) + l2 * np.sin(th1 + th2) + l3 * np.sin(th1 + th2 + th3)

plt.figure(2)
plt.plot(x.flatten(), y.flatten(), 'b.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
