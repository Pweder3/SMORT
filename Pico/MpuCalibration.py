import time
import adafruit_mpu6050 # type: ignore  
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore



sda_pin = board.GP16
scl_pin = board.GP17

i2c = busio.I2C(scl_pin, sda_pin)   

mpu = adafruit_mpu6050.MPU6050(i2c)

startTime = time.monotonic() # type: ignore
cTime = 10

finalValue = [0,0,0]

print("Calibrating...")

while time.monotonic() - startTime    < cTime :
    
    currentValues = mpu.acceleration
    
    
    for i in range(3):
        finalValue[i] += int(currentValues[i])
        

finalValue = [x/10 for x in finalValue]
print(finalValue)
