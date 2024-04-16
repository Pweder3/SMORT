import time
import adafruit_mpu6050 # type: ignore  
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
import array
import gc

t_array = array.array('f',[0])
x_array = array.array('f',[0])
y_array = array.array('f',[0])
z_array = array.array('f',[0])


sda_pin = board.GP16
scl_pin = board.GP17

i2c = busio.I2C(scl_pin, sda_pin)   

mpu = LSM6DSOX(i2c)

start_time = time.monotonic() # type: ignore

print("INNIT DONE")
with open("/data.csv", "a") as datalog:
    datalog.write(f" -----, ------, ------, -------, ------ \n")
    datalog.write(f"Time, X, Y, Z \n")
    lastTime = time.monotonic() # type: ignore
    while True:
        curTime = time.monotonic() # type: ignore
        difference_time = curTime - start_time
        
        
        t_array.append(difference_time) 
        x_array.append(round(mpu.acceleration[2],3))
        y_array.append(round(mpu.acceleration[2],3))
        z_array.append(round(mpu.acceleration[2],3)) 
       
        
        if difference_time > 30:
            break
        
        print(f"{(curTime - lastTime):.5f} sec, memfree: {gc.mem_free()}")
        lastTime = curTime
    datalog.write(f"{difference_time}, {x_array}, {y_array}, {z_array} \n")
        
        
        
            
        