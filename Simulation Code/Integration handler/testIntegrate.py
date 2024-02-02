import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid,trapz

order = 400
x = np.linspace(start= -10 , stop= 10,num= order)
y = 2*x



in1 = cumulative_trapezoid(y,dx= 20/order, initial=0)

fig, ax = plt.subplots()


# ax.plot(x, y )
ax.plot(x, y)
ax.plot(x, in1) 
# plt.ylim(-10,10)


plt.xlabel('Time')
plt.ylabel('Function Values')
plt.legend(['y = x**2', 'Integrated'])

plt.show()


