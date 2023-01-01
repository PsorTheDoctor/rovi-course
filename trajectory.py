import swift
import matplotlib.pyplot as plt
import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np

env = swift.Swift()
env.launch(realtime=True)

dt = 0.05
panda = rtb.models.Panda()
panda.q = panda.qr

# Tool space trajectories
t = panda.fkine(panda.q) * sm.SE3.Trans(0.2, 0.2, 0.35)
traj = rtb.ctraj(panda.fkine(panda.q), t, 100)
m = traj[len(traj) - 1] * sm.SE3.Trans(0, 0, -0.4)
traj.extend(rtb.ctraj(traj[len(traj) - 1], m, 50))

qik = panda.ikine_LM(traj, q0=panda.q)
tq = np.gradient(qik.q)

# Plot resulting trajectory
plt.figure(1)
plt.plot(tq[0])
plt.title('Joint velocities')

plt.figure(2)
plt.plot(tq[1])
plt.title('Joint positions')

env.add(panda)
# Visualize the path in simulation
for q in qik.q:
    panda.q = q
    env.step(dt)

# Joint space trajectories
curr = panda.q
dest = panda.qr
qtraj = rtb.jtraj(curr, dest, 20)

plt.figure(3)
plt.title('Joint velocities')
# Plot interpolated quaternion
plt.plot(qtraj.qd)

plt.figure(4)
plt.title('Joint positions')
# Plot interpolated quaternion
plt.plot(qtraj.q)

# Send trajectory to the robot arm
for qi in qtraj.q:
    panda.q = qi
    env.step(dt)

plt.show()
