
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz,trapz


def dbl_cumtrapz(x,y):
    r_array = np.zeros(len(x))
    for i in range(1, len(x)):
        r_array[i] =   y[i-1] +  (y[i-1] + y[i])/2 * (x[i] - x[i-1])
    r_array[0] = r_array[1] # normalize the first value 
    return r_array
        
        
x = np.linspace(0, 10, 100)

plt.plot(x, cumtrapz(np.cos(x),x,initial=0))
# plt.plot(x,np.sin(x))
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.legend(['cumtrapz','integrated','original'])
plt.show()