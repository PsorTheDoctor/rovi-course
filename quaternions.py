import numpy as np
from spatialmath import UnitQuaternion
from spatialmath.base import q2r, r2x, rotx, roty, rotz

v1 = [np.cos(np.deg2rad(90)/2), np.sin(np.deg2rad(90)/2), 0, 0]
v2 = [np.cos(np.deg2rad(-120)), 0, np.sin(np.deg2rad(-120)/2), 0]

Q1 = UnitQuaternion(v1)
print(Q1)

Q2 = UnitQuaternion(v2)
print(Q2)

R1 = rotx(90, 'deg')
R2 = roty(-120, 'deg')

Q3 = UnitQuaternion(R1)
print(Q1 == Q3)

Q4 = UnitQuaternion(R2)
print(Q2 == Q4)

Q5 = UnitQuaternion([1, 1, 0, 0])
Q6 = UnitQuaternion([2, 0, -2*np.sqrt(3), 0])

print('Normalized quaternions')
print(Q5.norm())
print(Q6.norm())

print('Sum of two quaternions', Q5 + Q6)
print('Subtraction of two quaternions', Q5 - Q6)
print('Multiplication', Q5 * Q6)
print('Multiplication', Q6 * Q5)
print('Division', Q5 * Q6.conj())
print('Division', Q6.conj() * Q5)

R = q2r(Q6.vec)
print(R)

rpy = r2x(R, representation='rpy/xyz')
print('RPY angles in degrees', np.rad2deg(rpy))
