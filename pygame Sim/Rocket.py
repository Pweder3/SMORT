from pygame import Vector2,time,image,draw,transform
import math
from dataclasses import dataclass




@dataclass
class RocketMotor:
    burnTime : int
    thrustPerSec: float 
    mass: float 
    
    def __post_init__(self) -> None:
        self.burnTime *= 1000
        


class Rocket():
    
    def __init__(self,clock: time.Clock, motor:RocketMotor,imageScale: int  ,rotation:float = math.pi/2, fps:int = 60) -> None:
        self.motor = motor
        self.clock = clock
        self.fps = fps
        self.rotation = rotation
        self.thrust = 0
        self.velocity = Vector2(math.cos(rotation),math.sin(rotation))
        self.position = [0,0]
        
        self.image = image.load("pygame Sim/RocketImage.png") # ik this is bad practice/no redundancy 
        newRect = int(self.image.get_rect()[2] * imageScale),int(self.image.get_rect()[3] * imageScale)
        self.image = transform.scale(self.image,newRect)
        
        
    def blitImage(self,screen):
        screen.blit(image, (self.position[0],self.position[1]))
    
    
    def currentMovementAngle(self) -> float:   
        return math.atan2(self.velocity[1],self.velocity[0])
    
    
    def getLocalizedPosition(self,position,screen_width,screen_height) -> tuple[int]:
        return (position[0] + (screen_width *.10) ,screen_height - position[1])
    
    def drawVelocity(self,screen,screen_width,screen_height):
        position = self.getLocalizedPosition(self.position,screen_width,screen_height)
        
        draw.line(screen,
                  (0,0,0),
                  position,
                  (position[0] + self.velocity[0] * 30,
                   position[1] - self.velocity[1] * 30),
                  5)
    
    def drawCircle(self,screen,screen_width,screen_height):
        position = self.getLocalizedPosition(self.position,screen_width,screen_height)
        
        draw.circle(screen,
                   (0,0,0),
                   position,
                   10)
    
        
    def update(self,tick,gravity = 0.1):
        
        currenttime = time.get_ticks()
        print(f"self.velocity: {self.velocity}, self.position: {self.position}, fuelTime: {(self.motor.burnTime ) > currenttime}")

        # TODO: make this structure better with the frame of refrence.
        
        if self.motor.burnTime > currenttime:
            
            
            self.thrust = (self.motor.thrustPerSec - gravity) * tick
            # As of "high level docs" https://pygame.org/wiki/2DVectorClass\
            
        else:
            self.thrust -= tick * gravity   
        
        # Frame of refrence is global here
        # TODO: make 0,0 the botom right corner
        self.velocity[0] = round(math.cos(self.rotation),2)
        self.velocity[1] = round(self.thrust * math.sin(self.rotation),2)

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        
    def getPosition(self) -> list[int]:
        return self.position
    
    def drawImage(self,screen,screen_width,screen_height):
        
        originPos = self.image.get_rect().center
        pos = self.getLocalizedPosition(self.position,screen_width,screen_height)
        angle =math.degrees(self.currentMovementAngle()) - 90
        
        
        # https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
        image_rect = self.image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = Vector2(pos) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        rotated_image = transform.rotate(self.image, angle)
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
        screen.blit(rotated_image, rotated_image_rect)
        
        
        
        