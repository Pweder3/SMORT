
from scipy.fft import fft, fftfreq,ifft
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
# plt.style.use('dark_background')

coeficent = 5

# Number of sample points
N = 10000 
# sample spacing
T = 1.0 / 800.0 
x = np.linspace(0.0, N*T, N,)
y = np.sin(2 * 2.0*np.pi*x) + 0.2*np.sin(50 * 2 *np.pi*x)
# y = np.sin(2 * 2.0*np.pi*x)

yf = fft(y)
xf = fftfreq(N, T)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(xf, np.abs(yf))
ax1.set_xlim(-60,60)
ax1.grid()
ax1.set_title('Fourier transform')

ax2.plot(y)
ax2.set_xlim(0,700)
ax2.grid()
ax2.set_title('Signal')

plt.subplots_adjust(hspace=0.5)
# plt.savefig('docs/Images/Images/fft_sin.png', dpi=300,transparent = True)
plt.show()


# example from https://docs.scipy.org/doc/scipy/tutorial/fft.html