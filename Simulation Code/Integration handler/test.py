
import matplotlib.pyplot as plt
import numpy as np


def integrate(x,y):
    r_array = np.zeros(len(x))
    for i in range(1, len(x)):
        r_array[i] =   y[i-1] +  (y[i-1] + y[i])/2 * (x[i] - x[i-1])
    return r_array
        
        
        
x = np.linspace(0, 4, num=100)
y = x**2
y_int = integrate(x,y)
plt.plot(x,y)
plt.plot(x,integrate(x,y), 'r')
plt.plot(x, x**3/3, 'g' )



# plt.plot(x,x**3/3)
plt.show()  