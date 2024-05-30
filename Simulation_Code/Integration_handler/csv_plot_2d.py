import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz,trapz,cumulative_trapezoid




def integrate_and_plot(path:str)->None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt



    # data = pd.read_csv(path,header= 0)
    data = pd.read_csv('Data/long_Form_Still_Data.csv',header= 0)



    t = data.iloc[:, 0].to_numpy() 
    x = data.iloc[:, 1].to_numpy() # +0.0655488
    y = data.iloc[:, 2].to_numpy()  #+0.0759979
    z = data.iloc[:, 3].to_numpy() # +4.72263


    xI1 = cumulative_trapezoid(x,t,initial=0)
    xI2 = cumulative_trapezoid(xI1,t,initial=0)
    
    yI1 = cumulative_trapezoid(y,t,initial=0)
    yI2 = cumulative_trapezoid(yI1,t,initial=0)
    
    zI1 = cumulative_trapezoid(z,t,initial=0)
    zI2 = cumulative_trapezoid(zI1,t,initial=0)


    
    fig, ax = plt.subplots(1,3)
    
    ax[0].plot(t,xI2,'b',label = 'x',)
    ax[1].plot(t,yI2,'g',label = 'y')
    ax[2].plot(t,zI2,'r',label = 'z')
    
    

    
    
    plt.show()

# path = "Data/2024-03-19 13:31:01.csv"
path = "Data/SIN_MOVE_ODR_DIV_800.csv"
integrate_and_plot(path)