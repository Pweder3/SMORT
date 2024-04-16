import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz,trapz
from scipy.fft import fft, fftfreq


path = "Data/SINCSV.csv"
data = pd.read_csv(path)


t = data.iloc[:, 0].to_numpy()
y = data.iloc[:, 1].to_numpy()

dx = 100/5000
yt = fft(y)
xf = fftfreq(y.size, dx)

fig, ax = plt.subplots()
plt.plot(xf, np.abs(yt))
plt.grid()
plt.show()