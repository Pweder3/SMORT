import time
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

import array
import gc
from mpl3115a2_highspeed import MPL3115A2

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

barometer = MPL3115A2(i2c)


start_time = time.monotonic() # type: ignore

print("INNIT DONE")

lastTime = time.monotonic() # type: ignore
index = 0


cut_off = 10

flag = True
while True:
    
    if all(abs(i) > cut_off for i in mpu.acceleration) or flag:
        flag = True
        curTime = time.monotonic() # type: ignore
        difference_time = curTime - start_time

        if len(t_array) < 2000:
            t_array.append(difference_time) 
            x_array.append(round(mpu.acceleration[0],3))
            y_array.append(round(mpu.acceleration[1],3))
            z_array.append(round(mpu.acceleration[2],3)) 
            barr_array.append(round(barometer.pressure,2))


        else:
            t_array[index] = difference_time
            x_array[index] = round(mpu.acceleration[0],3)
            y_array[index] = round(mpu.acceleration[1],3)
            z_array[index] = round(mpu.acceleration[2],3)
            barr_array[index] = round(barometer.pressure,2)

            index +=1
            if index > 2000:
                index = 0

        i = len(t_array)-1
        print(f"{t_array[i]} {x_array[i]} {y_array[i]} {z_array[i]} {barr_array[i]}")

        if difference_time > 20:
            print("finished")
            flag = False
            with open("/data.csv", "a") as datalog:
                datalog.write(f" -----, ------, ------, -------, ------ \n")
                datalog.write(f"Time, X, Y, Z, A \n")
                for x in range(len(t_array)):
                    datalog.write(f"{t_array[x]}, {x_array[x]}, {y_array[x]}, {z_array[x]}, {barr_array[x]} \n")
                    # prob a builtin way to do this but i dont have time to find it.
                t_array = array.array('f',[0])
                x_array = array.array('f',[0])
                y_array = array.array('f',[0])
                z_array = array.array('f',[0])
                barr_array = array.array('f',[0])
                
        
        ## 
    
        # print(f"{(curTime - lastTime):.5f} sec, memfree: {gc.mem_free()}, {len(t_array)}")
        lastTime = curTime


        
        
            
        