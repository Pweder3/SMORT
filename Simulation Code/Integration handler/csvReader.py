import numpy as np
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Simulation Code\Integration handler\data.csv',)


x = data['Time'].to_numpy()
y = data['x'].to_numpy()


def integrate(x, y):
    return np.array([np.trapz(y[:i],x= x[:i] ) for i in range(x.size) ])

int1 =  integrate(x, y)
int2 =  integrate(x,int1)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.plot(x, int1)
ax.plot(x, int2)

plt.legend(['acceleration','velocity', 'positon'])

plt.show()



