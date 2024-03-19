import serial,string
import pandas as pd
from ast import literal_eval as make_tuple
import matplotlib.pyplot as plt
import traceback
from pathlib import Path
from datetime import datetime
import time

serial = serial.Serial('/dev/tty.usbmodem141301', 115200, timeout=1)

serial.close()

df = pd.DataFrame(dict(zip(["t","x",'y','z'],[0,0,0,0])), index = [0])

start_time = time.time()
with serial as serial:
    for x in range (1000):
        serail_in = serial.readline().decode('utf-8')
        try:
            dt = time.time() - start_time
            data = pd.DataFrame(dict(zip(["t","x",'y','z'], list(make_tuple(serail_in)))),index = [0]) # type: ignore
            df = pd.concat([df,data]).reset_index(drop = True)
        except Exception as e:
            # traceback.print_exc()
            # print(f"error:")
            continue
        
df.drop(index=0, inplace = True) # type: ignore
df.reset_index(drop = True, inplace = True)
normaliseValue = df["t"][0]
df['t'] -= normaliseValue


name = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.csv"
csv_path = (Path(__file__).parent.parent) / "Data" / name
df.to_csv(csv_path, index = False)
        

def integrate_and_plot(path:str)->None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt



    data = pd.read_csv(path,header= 0)
    # data = pd.read_csv('Simulation Code/Integration handler/accelerometer_data.csv',header= 0)



    t = data.iloc[:, 0].to_numpy() 
    x = data.iloc[:, 1].to_numpy() # +0.0655488
    y = data.iloc[:, 2].to_numpy()  #+0.0759979
    z = data.iloc[:, 3].to_numpy() # +4.72263




    def integrate(x,y):
        r_array = np.zeros(len(x))
        for i in range(1, len(x)):
            r_array[i] =   y[i-1] +  (y[i-1] + y[i])/2 * (x[i] - x[i-1])
        r_array[0] = r_array[1] # normalize the first value 
        return r_array


    xI1 = integrate(t, x)
    xI2 = integrate(t,xI1)

    plt.plot(t,x,'r')
    plt.plot(t,xI1,'g')
    plt.plot(t,xI2,'b')
    plt.legend(['acceleration','velocity', 'positon'])
    plt.title('Position while still')
    plt.show()


integrate_and_plot(csv_path)
    