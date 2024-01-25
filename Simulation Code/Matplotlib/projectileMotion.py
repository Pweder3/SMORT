from matplotlib import pyplot as plt
import numpy as np

def integrate(x, y):
    return np.array([np.trapz(y[:i],x= x[:i] ) for i in range(x.size) ])

fig,ax = plt.subplots()

t = np.linspace(0,10,1000)
y =   integrate(t, integrate(t, (1/2*t**2 * -9.81)))  +5

# plt.ylim(0,10)
ax.plot(t,y)
plt.show()