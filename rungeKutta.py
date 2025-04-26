import numpy as np
import matplotlib.pyplot as plt

g = 9.81
m = 0.145
k = 0.01
theta = np.radians(45)
v0 = 50
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)

def derivatives(state):
    x, y, vx, vy = state
    v = np.sqrt(vx**2 + vy**2)
    ax = -k * v * vx / m
    ay = -g - (k * v * vy / m)
    return np.array([vx, vy, ax, ay])

dt = 0.01
state = np.array([0.0, 0.0, vx0, vy0])
trajectory = [state[:2]]

while state[1] >= 0:
    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)
    state = state + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)
    trajectory.append(state[:2])

trajectory = np.array(trajectory)
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion with Air Resistance')
plt.grid()
plt.show()
