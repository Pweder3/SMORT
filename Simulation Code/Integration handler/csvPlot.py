import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz,trapz

# Read the CSV file
# data = pd.read_csv('Simulation Code/Integration handler/accelerometer_data.csv',header= 0)

data = pd.read_csv('Simulation Code/Integration handler/data.csv',header= 0)


t = data.iloc[:, 0].to_numpy()
x = data.iloc[:, 1].to_numpy()
y = data.iloc[:, 2].to_numpy()
z = data.iloc[:, 3].to_numpy()

def integrate(x, y):
    return np.array([np.trapz(y[:i],x= x[:i] ) for i in range(x.size) ])

xI1 =  cumtrapz(t, x, initial=0)
xI2 =  cumtrapz(t,xI1,initial=0)

yI1 =  cumtrapz(t, y, initial=0)
yI2 =  cumtrapz(t,yI1,initial=0)

zI1 =  cumtrapz(t, z, initial=0)
zI2 =  cumtrapz(t,zI1,initial=0)


# fig, ax = plt.subplots()
ax = plt.figure().add_subplot(projection = "3d")
ax.plot(x,y,zs =z)
ax.plot(xI1, yI1, zs = zI1, color = 'red')
ax.plot(xI2, yI2, zs = zI2, color = 'green')

plt.legend(['acceleration','velocity', 'positon'])

plt.show()



