# Dump
- we need to calulate in the loss of fuel mass as the rocket is launched to change the effect on the rockets velocity and eventual positon
-  innital rocket vector is defined as $\vec{V} = v$
- $\hat{i}$ is a unit vector in the x direction 

#  basic simulation of a rocket launch
 - We dont need spacififcs of the rocket mass or fuel mass because our rocket motor is so little mass compared to the rocket
 - We can just use the burn time of the rocket use a initial inerta to calculate the final velocity of the rocket and then subtract the gravity constant. 


# [wiki Dump](https://en.wikipedia.org/wiki/Projectile_motion)
  - Maximum horrizontal distance formula
-  $$ d = \frac{v^2 \cos(\theta)}{g} \left( v \sin{\theta} +  \sqrt{ v^2 \sin^2({\theta}) +2gy_{0} } \right) $$
  
  
  
# Program ideas
for the final we can use matplot lib for projected path and then use a CSV file to get the actuall path similar to a basic velecity trajectory $\downarrow$
![[Figure_1.png|400]]


- Dont make it to complicated just use it for documentation and to learn the math for the actual calculation



# MPU 6050 Calibration
The mpu calibration had to be done to make sure that the values that are saved are accurate for a long period of tine and makes sure that when we double integrate the values later after we collect the csv file that the values are accurate.

<img src = "https://github.com/Pweder69/SMORT/blob/main/docs/Images/Images/Final%20Calibration.png">

Final calibration in rad/s: [-0.02095, -0.01645, 0.0104]


## replication of the calibration
to calibrate you can follow [this](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sensorlab-magnetometer-calibration.pdf) tourtial from adafruit. Use a metro M4 (i used an airlift) not a py pico because the pico doesnt use an EPROMM and that is needed to run the calibration code. To install the dependancies for python run the following commands in the terminal

- `pip3 install matplotlib`
- `pip3 install pyserial`
- `pip3 install numpy`

Note that some may have to **use python 3.11 or lower** to install the dependancies.
To find the serial port that the metro is connected to use the arduino IDE and go to tools and then port and it should be the one listed under your board.


---
# Reasorces

- [Rocket Equations](https://www.grc.nasa.gov/WWW/K-12/rocket/rktpow.html)
- <a href="https://pressbooks.online.ucf.edu/osuniversityphysics/chapter/9-7-rocket-propulsion/#:~:text=mim).-,%CE%94%20v%20%3D%20u%20ln%20(%20m%20i%20m%20)%20.,m0%20down%20to%20m.">Press Books text</a>
- [Fourm](https://www.physicsforums.com/threads/how-to-calculate-the-trajectory-of-a-mortar-round.293783/)
- [Projectile motion wikipedia](https://en.wikipedia.org/wiki/Projectile_motion#Trajectory_of_a_projectile_with_air_resistance)
- [Projectile distance Wiki](https://en.wikipedia.org/wiki/Range_of_a_projectile)