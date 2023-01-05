import roboticstoolbox as rtb
import numpy as np
# import spatialmath as sm
from spatialmath import SE3
import swift
import spatialgeometry as sg

env = swift.Swift()
env.launch(realtime=True)

ur5 = rtb.models.UR5()
print(ur5)

# Initial configuration of the robot arm
q0 = [-np.pi/2, -np.pi/2, -np.pi/2, -np.pi/2, np.pi/2, 0]
q1 = [-np.pi/2, -np.pi/2, -np.pi/2, 0, np.pi/2, 0]

# Calculate robot forward kinematics
print(ur5.fkine(q0))

# Sample pick position defined in tool space
target = SE3.Trans(-0.464, -0.436, 0.202) * SE3.RPY(-3.1416, 0, 3.1416, order='zyx')
print(target)

# Define a pose marker for display purposes
marker = sg.Axes(0.1, pose=target)
marker.pose = target

# Add robot and marker to the environment
env.add(ur5)
env.add(marker)

# Visualize the robot
ur5.q = q0
env.step()

input('Press enter to continue...')

# Inverse kinematics
ik = ur5.ikine_LM(target, q0=q0)
print(ik.q)
ur5.q = ik.q

# Visualize
env.step()

input('Press enter to finish...')
