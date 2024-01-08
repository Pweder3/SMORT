from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
theta = np.cos(np.radians(0))

z = g * t**2 / 2 + (v0 * t) * theta



line = ax.plot(t, z, label=f'v0 = {v0} m/s')[0]
plt.show()