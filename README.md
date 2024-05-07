# S.M.O.R.T. PROJECT 
**Smart, Modular, Off-axis, Reloadable, Tube-launcher**

## Table of Contents



* [Planning](#Planning) 
* [Materials](#Materials)
* [CAD](#CAD)
* [Photos of the Shell and Cannon](#Photos)
* [Circuit Diagram](#Circuit_Diagram)
* [Code](#Code)
* [Failed launches and other issues](#Failures)
* [Plotted Data and Analysis](#Plotted_Data+Analysis)
* [Final Version](#Final_Version)



# Planning 
Here is a more detailed planning document[LINK](https://github.com/Pweder3/SMORT/tree/main/Documentation/Planning).
# Materials
_a long list of everything we needed for our project. even if it isn't in the final project it should be listed with a note that says why it didn't stick_ 
_

# CAD
Here is a link to more detailed documentation of our CAD process [LINK](https://github.com/Pweder3/SMORT/tree/main/Documentation/CAD).
Here is a link to our OnShape document where you can directly look at our CAD [LINK](https://github.com/Pweder3/SMORT/blob/main/Documentation/CAD/OnshapeLink.md)

<img src = "https://github.com/Pweder3/SMORT/blob/main/Documentation/Images/Images/Deployable%20Fins%20Packed.png" width = 500>
Here is a picture of our fin design in the folded position
<img src = "https://github.com/Pweder3/SMORT/blob/main/Documentation/Images/Images/Deployable%20Fins%20Image.png" width = 500>
This is a picture of our fins in the deployed position


# Photos

_photos that we took during the building process
_
# Circuit Diagram



# Code

## Replication of the calibration
to calibrate you can follow [this](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sensorlab-magnetometer-calibration.pdf) tourtial from adafruit. Use a metro M4 (I used an airlift) not a pico because it doesnt seem to be able to run the code given in the tutorial. Another thing to note is that you need a certain amount of program mem that things like the Arduino UNO don't have. To install the dependencies for Python run the following commands in the terminal

- `pip3 install matplotlib`
- `pip3 install pyserial` (Although the import message says import serial it is part of the pyserial package, not the serial package)
- `pip3 install numpy`

Note that some may have to **use Python 3.11 or lower** because of import changes in 3.12. To find the serial port that the metro is connected to use the Arduino IDE and go to tools and then port and it should be the one listed under your board. Also, note that this info is all our teams issues with the tutorial and the problems that we had.

# Failures
We had many failed launch attempts with our rocket-propelled shells and we have more documentation of those attempts here [More Launch Info](https://github.com/Pweder3/SMORT/blob/main/Documentation/Launch%20Documentation.md)


## Tube Fire
<img src = "https://github.com/Pweder69/SMORT/blob/48975b8509867a4feda575c4828a8f50840fb580/Documentation/Images/Images/ignition1.gif" width =300>
<img src = "https://github.com/Pweder69/SMORT/blob/main/Documentation/Images/Images/fullbody.ignition1.jpg" width =500>
<img src = "https://github.com/Pweder69/SMORT/blob/main/Documentation/Images/Images/endcap.ignition1.jpg" width =200><img src = "https://github.com/Pweder69/SMORT/blob/main/Documentation/Images/Images/tubeview.ignition1.jpg" width =200>


# Plotted_Data+Analysis

# Final_Version

_needs to include the best videos we have of our final launch as well as a picture of the rocket and cannon fully assembled
_
