# Dump
- we need to calulate in the loss of fuel mass as the rocket is launched to change the effect on the rockets velocity and eventual positon
-  innital rocket vector is defined as $\vec{V} = v$
- $\hat{i}$ is a unit vector in the x direction 

##  basic simulation of a rocket launch
 - We dont need spacififcs of the rocket mass or fuel mass because our rocket motor is so little mass compared to the rocket
 - We can just use the burn time of the rocket use a initial inerta to calculate the final velocity of the rocket and then subtract the gravity constant. 


# [wiki Dump](https://en.wikipedia.org/wiki/Projectile_motion)
  - Maximum horrizontal distance formula
-  $$d = \frac{v^2 \cos(\theta)}{g} \left( v \sin{\theta} +  \sqrt{ v^2 \sin^2({\theta}) +2gy_{0} } \right)$$
  
  
  
# Program ideas
for the final we can use matplot lib for projected path and then use a CSV file to get the actuall path similar to a basic velecity trajectory $\downarrow$

<img src ="https://github.com/Pweder69/SMORT/blob/3752453b33a51189e40eb2611e1eebf9fd58bc50/docs/Images/Images/Figure_1.png" width =400>


- Dont make it to complicated just use it for documentation and to learn the math for the actual calculation



# MPU 6050 Calibration
The mpu calibration had to be done to make sure that the values that are saved are accurate for a long period of tine and makes sure that when we double integrate the values later after we collect the csv file that the values are accurate.

<img src = "https://github.com/Pweder69/SMORT/blob/main/docs/Images/Images/Final%20Calibration.png">

Final calibration in rad/s: [-0.02095, -0.01645, 0.0104]
Second MPU CALIBRATION [-0.0317, -0.0109, -0.0196]


---
# Reasorces

- [Rocket Equations](https://www.grc.nasa.gov/WWW/K-12/rocket/rktpow.html)
- <a href="https://pressbooks.online.ucf.edu/osuniversityphysics/chapter/9-7-rocket-propulsion/#:~:text=mim).-,%CE%94%20v%20%3D%20u%20ln%20(%20m%20i%20m%20)%20.,m0%20down%20to%20m.">Press Books text</a>
- [Fourm](https://www.physicsforums.com/threads/how-to-calculate-the-trajectory-of-a-mortar-round.293783/)
- [Projectile motion wikipedia](https://en.wikipedia.org/wiki/Projectile_motion#Trajectory_of_a_projectile_with_air_resistance)
- [Projectile distance Wiki](https://en.wikipedia.org/wiki/Range_of_a_projectile)