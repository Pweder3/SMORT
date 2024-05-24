import time
import adafruit_lsm6ds # type: ignore
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX # type: ignore
import adafruit_mpl3115a2



sda_pin = board.GP16
scl_pin = board.GP17

# i2c = busio.I2C(scl_pin, sda_pin)  
i2c = board.STEMMA_I2C() 


mpu = LSM6DSOX(i2c)

start_time = time.monotonic() # type: ignore
data_amount = 0
data_list = [[],[],[]]

while True:
    curTime = time.monotonic() # type: ignore
    difference_time = curTime - start_time
    
    
    acceleration = mpu.acceleration
    rounded_values = [round(x,3) for x in acceleration ] 
    # 0x6a
    # 0.768448, 0.181718, -1.70216
    
    data_list[0].append(rounded_values[0] -0.768448)
    data_list[1].append(rounded_values[1]-0.182517)
    data_list[2].append(rounded_values[2] +1.70052)
    
    
    
    data_amount +=1
    
    if round(difference_time,1) % 2 == 0:
        for i in range(len(data_list)):
            print(f" X: {data_list[i][0]:.2f}, Y: {data_list[i][1]:.2f}, Z: {data_list[i][2]:.2f}")
        
        data_list = [[],[],[]]
    
        