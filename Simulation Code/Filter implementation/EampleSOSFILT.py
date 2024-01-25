import matplotlib.pyplot as plt
from scipy import signal
b, a = signal.ellip(13, 0.009, 80, 0.05, output='ba')
sos = signal.ellip(13, 0.009, 80, 0.05, output='sos')
x = signal.unit_impulse(700)
y_tf = signal.lfilter(b, a, x)
y_sos = signal.sosfilt(sos, x)
plt.plot(y_tf, 'r', label='TF')
plt.plot(y_sos, 'k', label='SOS')
plt.legend(loc='best')
plt.show()
