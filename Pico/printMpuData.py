import time
import adafruit_lsm6ds
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX



sda_pin = board.GP16
scl_pin = board.GP17

i2c = busio.I2C(scl_pin, sda_pin)   


mpu = LSM6DSOX(i2c)

start_time = time.monotonic() # type: ignore
pString = ""
data_amount = 0

while True:
    curTime = time.monotonic() # type: ignore
    difference_time = curTime - start_time
    
    
    acc = mpu.acceleration
    added = [round(x,3) for x in acc ] 
    # 0x6a
    
    # 0.768448, 0.181718, -1.70216
    
    
    roundValue = 2
    pString += f" {curTime}, {added[0] -0.768448}, {added[1]-0.182517}, {added[2] +1.70052}, " + "\n"
    data_amount +=1
    
    if round(difference_time,1) % 2 == 0:
        print(pString)
        pString = ""
    
        