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
        

from Simulation_Code.Integration_handler.csv_plot_2d import integrate_and_plot

integrate_and_plot(csv_path)
    
    
    
