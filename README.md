# S.M.O.R.T. PROJECT 
**Smart, Modular, Off-axis, Reloadable, Tube-launcher**

## Table of Contents



* [Planning](#Planning) 
* [Materials](#Materials)
* [CAD](#CAD)
* [Photos of the Shell and Cannon](#Photos_of_the_Shell_and_Cannon)
* [Circuit Diagram](#Circuit_Diagram)
* [Code](#Code)
* [Failed launches and other issues](#Failed_launches_and_other_issues)
* [Plotted Data and Analysis](#Plotted_Data_and_Analysis)
* [Best Videos of the Final Launch](#Best_Videos_of_the_Final_Launch)



# Planning 

# Materials

# CAD

# Photos of the Shell and Cannon

# Circuit Diagram

# Code

## Replication of the calibration
to calibrate you can follow [this](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sensorlab-magnetometer-calibration.pdf) tourtial from adafruit. Use a metro M4 (I used an airlift) not a pico because it doesnt seem to be able to run the code given in the tutorial. Another thing to note is that you need a certain amount of program mem that things like the Arduino UNO don't have. To install the dependencies for Python run the following commands in the terminal

- `pip3 install matplotlib`
- `pip3 install pyserial` (Although the import message says import serial it is part of the pyserial package, not the serial package)
- `pip3 install numpy`

Note that some may have to **use Python 3.11 or lower** because of import changes in 3.12. To find the serial port that the metro is connected to use the Arduino IDE and go to tools and then port and it should be the one listed under your board. Also, note that this info is all our teams issues with the tutorial and the problems that we had.

# Failed Launches and other Issues


# Plotted Data and Analysis

# Best Videos of the Final Launch
