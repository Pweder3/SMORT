import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz,trapz

data = pd.read_csv('Simulation Code/Integration handler/data.csv',header= 0)
# data = pd.read_csv('Simulation Code/Integration handler/accelerometer_data.csv',header= 0)



t = data.iloc[:, 0].to_numpy() 
x = data.iloc[:, 1].to_numpy() # +0.0655488
y = data.iloc[:, 2].to_numpy()  #+0.0759979
z = data.iloc[:, 3].to_numpy() # +4.72263




def integrate(x,y):
    r_array = np.zeros(len(x))
    for i in range(1, len(x)):
        r_array[i] =   y[i-1] +  (y[i-1] + y[i])/2 * (x[i] - x[i-1])
    r_array[0] = r_array[1] # normalize the first value 
    return r_array
        
        
xI1 = integrate(t, x)
xI2 = integrate(t,xI1)

plt.plot(t,x,'r')
# plt.plot(t,xI1,'g')
# plt.plot(t,xI2,'b')
plt.legend(['acceleration','velocity', 'positon'])
plt.show()