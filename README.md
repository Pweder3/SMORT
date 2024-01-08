# S.M.O.R.T. PROJECT 
**Smart, Modular, Off-axis, Reloadable, Tube-launcher**

## Table of Contents

* [CAD](#CAD)
* [Code](#Code)
* [Tests](#Tests)
* [Final_Project](#Final-Project)




## replication of the calibration
to calibrate you can follow [this](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sensorlab-magnetometer-calibration.pdf) tourtial from adafruit. Use a metro M4 (i used an airlift) not a py pico because it doesnt seem to be able to run the code given in the tutorial. Another thing to note is that you need a cirtain amount of prgram mem that things like the Arduino uno dont have. To install the dependancies for python run the following commands in the terminal

- `pip3 install matplotlib`
- `pip3 install pyserial` (Although the import message says import serial its part of the pyserial package not the serial package)
- `pip3 install numpy`

Note that some may have to **use python 3.11 or lower** becasue of import changes in 3.12.To find the serial port that the metro is connected to use the arduino IDE and go to tools and then port and it should be the one listed under your board.

