import numpy as np
from spatialmath import UnitQuaternion
import matplotlib.pyplot as plt


def plot_Q_interp(Q_interp):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='y', alpha=0.1)
    ax.plot(Q_interp.vec[..., 0], Q_interp.vec[..., 1], Q_interp.vec[..., 2], c='k')
    plt.show()


v1 = [np.cos(np.deg2rad(90)/2), np.sin(np.deg2rad(90)/2), 0, 0]
v2 = [np.cos(np.deg2rad(-120)), 0, np.sin(np.deg2rad(-120)/2), 0]

Q1 = UnitQuaternion(v1)
Q2 = UnitQuaternion(v2)

# Quaternion interpolation
samp = 100
Q_interp = Q1.interp(Q2, samp)
print(Q_interp.vec)

Q1.plot(frame='A', color='green')
Q2.plot(frame='B', color='red')

# Plot interpolated quternion
plot_Q_interp(Q_interp)
