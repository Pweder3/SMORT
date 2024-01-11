import  numpy as np
import matplotlib.pyplot as plt


def integrate(x, y):
    return np.array([np.trapz(y[:i],x= x[:i] ) for i in range(x.size) ])


# Define the parameters for the simple harmonic motion
omega = 2 * np.pi  # angular frequency, in rad/s
x_max = 1.0  # maximum displacement, in m
t_end = 1.0  # end time, in s
dt = 0.01  # time step, in s

# Generate the time values
t = np.arange(0, t_end, dt)

# Generate the displacement values
x = x_max * np.cos(omega * t)

# Calculate the acceleration values
a = -omega**2 * x




fig, ax = plt.subplots()


ax.plot(t, a)
ax.plot(t, integrate(t,integrate(t,x)))

plt.show()