import roboticstoolbox as rtb
import numpy as np
import swift

jointPoses = [
  [-np.pi/2, -np.pi/2, -np.pi/2, -np.pi/2, np.pi/2, 0],
  [-np.pi/2, -np.pi/2, -np.pi/2, 0, np.pi/2, 0],
  [np.deg2rad(0), np.deg2rad(-30), np.deg2rad(0), np.deg2rad(30), np.deg2rad(30), np.deg2rad(0)],
  [np.deg2rad(0), np.deg2rad(-120), np.deg2rad(120), np.deg2rad(-90), np.deg2rad(0), np.deg2rad(0)],
  [np.deg2rad(0), np.deg2rad(-45), np.deg2rad(-90), np.deg2rad(0), np.deg2rad(0), np.deg2rad(0)],
]

env = swift.Swift()
env.launch(realtime=True)

ur5 = rtb.models.UR5()
env.add(ur5)

ur5.q = jointPoses[0]
env.step()

# Calculate jacobian in the base frame
jac = ur5.jacob0(jointPoses[0])
print('Jacobian', jac)

# Calculate the determinant of the jacobian
print('Determinant', np.linalg.det(jac))

# Check jacobian singularity
print('Is the jacobain singular?', rtb.jsingu(jac))

input('Press enter to continue...')
