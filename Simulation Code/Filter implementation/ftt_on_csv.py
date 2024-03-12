import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz,trapz
from scipy.fft import fft, fftfreq


data = pd.read_csv('Simulation Code/Integration handler/data.csv',header= 0)


t = data.iloc[:, 0].to_numpy()
y = data.iloc[:, 1].to_numpy()


yt = fft(y)
xf = fftfreq(y.size, t[1]-t[0])

fig, ax = plt.subplots()
plt.plot(xf, np.abs(yt))
plt.grid()
plt.show()