import pygame
from Rocket import Rocket
from Rocket import RocketMotor
import math

pygame.init()
screenDimentions = (screen_width, screen_height) = (2000, 600)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robotics Simulator")
clock = pygame.time.Clock()

def relTiv(position):
    return (position[0] + (screen_width *.10) ,screen_height - position[1])

motor = RocketMotor(2,200,3)

rocket = Rocket(clock,motor,.2,rotation= math.pi/6)


while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
            
    screen.fill((255,255,255))
    rocket.update(clock.tick()/1000,gravity=.5)
    
    
    # rocket.drawCircle(screen,screen_width,screen_height)
    # rocket.drawVelocity(screen,screen_width,screen_height)
    
    rocket.drawImage(screen,screen_width,screen_height)
    
    pygame.display.update()
    