from matplotlib import pyplot as plt
import numpy as np
import math
import random


t = np.linspace(0, 10, 1000)

x = np.zeros(len(t))
for i in range(len(t)-1):
   x[i] =  np.sin(i) + (random.randrange(-50, 50))

for f in range(200,270):
    x[f]= x[199]

plt.plot(t, x)

plt.show()