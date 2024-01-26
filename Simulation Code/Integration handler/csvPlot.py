import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz,trapz

# Read the CSV file
# data = pd.read_csv('Simulation Code/Integration handler/accelerometer_data.csv',header= 0)

data = pd.read_csv('Simulation Code/Integration handler/data.csv',header= 0)


t = data.iloc[:, 0].to_numpy()
y = data.iloc[:, 1].to_numpy()


def integrate(x, y):
    return np.array([np.trapz(y[:i],x= x[:i] ) for i in range(x.size) ])

int1 =  cumtrapz(t, y, initial=0)
int2 =  cumtrapz(t,int1,initial=0)

fig, ax = plt.subplots()

ax.plot(t, y)
ax.plot(t, int1)
ax.plot(t, int2)

plt.legend(['acceleration','velocity', 'positon'])

plt.show()



