import pygame
from Rocket import Rocket,RocketMotor,grid,smokeTrail

import math

pygame.init()
screenDimentions = (screen_width, screen_height) = (2000, 600)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robotics Simulator")
clock = pygame.time.Clock()


screenGrid = grid(screen_width,screen_height,50)

motor = RocketMotor(3,200,3)    

rocket = Rocket(clock,motor,.2,rotation= math.pi/6)


while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
            
    screen.fill((255,255,255))
    tick = clock.tick_busy_loop(60)/1000 
    
    rocket.update(tick)
    
    # all mesurements are within the scope of pixles per second for example gravity is 100 pixles per second
    
    screenGrid.draw(screen,1)
    
    rocket.drawImage(screen,screen_width,screen_height)
     
     
    localizedpos = rocket.getLocalizedPosition(rocket.position,screen_width,screen_height)
    # this is a bad way to do this but it works for now should default pos
    
    pygame.display.update()
    