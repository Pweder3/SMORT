import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

order = 300
x = np.linspace(start= 0, stop= 20,num= order)
y = 2*x**2 - 2*x+1


integrated = np.array([np.trapz(y[:i],x= x[:i] ) for i in range(order) ])  


def integrate(x, y):
    return np.array([np.trapz(y[:i],x= x[:i] ) for i in range(x.size) ])

fig, ax = plt.subplots()


# ax.plot(x, y )
ax.plot(x, y)
ax.plot(x, integrated) 
plt.ylim(0,10)


plt.xlabel('Time')
plt.ylabel('Function Values')
plt.legend(['y = x**2', 'Integrated'])

plt.show()


