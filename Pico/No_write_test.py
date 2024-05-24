import time
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
import array
import gc
import adafruit_mpl3115a2

t_array = array.array('f',[0])
x_array = array.array('f',[0])
y_array = array.array('f',[0])
z_array = array.array('f',[0])
barr_array = array.array('f',[0])

# sda_pin = board.GP16
# scl_pin = board.GP17

# i2c = busio.I2C(scl_pin, sda_pin)   
i2c = board.STEMMA_I2C()

mpu = LSM6DSOX(i2c)

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)


start_time = time.monotonic() # type: ignore

print("INNIT DONE")

lastTime = time.monotonic() # type: ignore
index = 0




while True:
    curTime = time.monotonic() # type: ignore
    difference_time = curTime - start_time
    print(f"{difference_time[-1]}, {x_array[-1]}, {y_array[-1]}, {z_array[-1]}, {barr_array[-1]} \n")
    if len(t_array) < 1800:
        t_array.append(difference_time) 
        x_array.append(round(mpu.acceleration[2],3))
        y_array.append(round(mpu.acceleration[2],3))
        z_array.append(round(mpu.acceleration[2],3)) 
        barr_array.append(round(sensor.pressure,2))
        
    else:
        t_array[index] = difference_time
        x_array[index] = round(mpu.acceleration[0],3)
        y_array[index] = round(mpu.acceleration[1],3)
        z_array[index] = round(mpu.acceleration[2],3)
        barr_array[index] = round(sensor.pressure,2)
        
        index +=1
        if index > 1799:
            index = 0
    
    if difference_time > 30:
        break
    
    ## 
   
    # print(f"{(curTime - lastTime):.5f} sec, memfree: {gc.mem_free()}, {len(t_array)}")
    lastTime = curTime
    
        
        
        
            
        