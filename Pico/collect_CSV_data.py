import serial,string
import pandas as pd
from ast import literal_eval as make_tuple
import matplotlib.pyplot as plt

serial = serial.Serial('/dev/tty.usbmodem141201', 115200, timeout=1)

serial.close()

df = pd.DataFrame(  columns = ["x",'y','z'] )


with serial as serial:
    for x in range (100):
        data = make_tuple(serial.readline().decode('utf-8'))
        df.loc[x] = data
        

plt.plot(df.loc[:,"x"].to_numpy())

    
    
    
