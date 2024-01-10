import time 
import adafruit_mpu6050 # type: ignore   
import busio # type: ignore 
import board # type: ignore 
import digitalio # type: ignore 
 
 
 
sda_pin = board.GP16
scl_pin = board.GP17 
 
i2c = busio.I2C(scl_pin, sda_pin)    
 
mpu = adafruit_mpu6050.MPU6050(i2c) 
 
led = digitalio.DigitalInOut(board.LED) 
 
 
for x in [led]: 
    x.direction = digitalio.Direction.OUTPUT 
 
 
with open("/data.csv", "a") as datalog: 
    #this line opens the file data.txt and appends info to the end of it 
    datalog.write(f" -----, ------, ------, -------, ------ \n") 
    while True: 
        curTime = time.monotonic() # type: ignore 
         
        acc = mpu.acceleration 
 
        added = [round(x,3) for x in acc ]  
         
        
        
        datalog.write(f" {curTime}, {added[0]}, {added[1]}, {added[2]} \n") 
         
        datalog.flush() 
        led.value = True 
        time.sleep(0.25) 
        led.value = False 
        time.sleep(0.25) 