from pygame import Vector2,time,image,draw,transform,font
import math
import random
from dataclasses import dataclass




@dataclass
class RocketMotor:
    burnTime : int
    thrustPerSec: float 
    mass: float 
    
    def __post_init__(self) -> None:
        self.burnTime *= 1000
        


class Rocket():
    
    def __init__(self,clock: time.Clock, motor:RocketMotor,imageScale: int  ,rotation:float = math.pi/6,isTrail: bool = True ) -> None:
        self.motor = motor
        self.clock = clock
        self.startTime = time.get_ticks()
        self.trail = smokeTrail()
        self.rotation = rotation
        self.thrust = 0
        self.velocity = Vector2(math.cos(rotation),math.sin(rotation))
        self.position = [0,0]
        self.gravity = 5
        
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
    
        
    def update(self,tick,):
        
        
        if self.position[1] > -20:
            
        
        
            currenttime = time.get_ticks()


            # TODO: make this structure better with the frame of refrence.

            if self.motor.burnTime > currenttime:

                print(f"self.velocity: {self.velocity}, self.position: {self.position}, fuelTime: {(self.motor.burnTime ) > currenttime} thrust: {self.thrust}" )

                self.thrust = (self.motor.thrustPerSec - self.gravity)
                # As of "high level docs" https://pygame.org/wiki/2DVectorClass\

            else:

                self.gravity *= 1 + (1 * tick)
                print(self.gravity)  



            draggCoeffiecnet = 0.5

            self.velocity[0] =  math.cos(self.rotation) * (self.thrust -draggCoeffiecnet ) * tick


            self.velocity[1] =  (math.sin(self.rotation) *  self.thrust - self.gravity ) * tick

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
        
        
        self.trail.draw(screen,pos,5)
        screen.blit(rotated_image, rotated_image_rect)
        
        
        
class grid:
        
        def __init__(self,screen_width,screen_height,gridSize) -> None:
            self.screen_width = screen_width
            self.screen_height = screen_height
            self.gridSize = gridSize
            
        def draw(self,screen,labelWorth = None):
            for x in range(0,self.screen_width,self.gridSize):
                draw.line(screen,
                        (0,0,0),
                        (x,0),
                        (x,self.screen_height))
                
            for y in range(0,self.screen_height,self.gridSize):
                draw.line(screen,
                        (0,0,0),
                        (0,y),
                        (self.screen_width,y))
            
            if labelWorth is not None:
                text = font.SysFont("Arial", 10)
                
                for x in range(self.screen_width // self.gridSize):
                    textAsSurface =  text.render(str(x * labelWorth),True,(0,0,0))
                    screen.blit(textAsSurface,(x * self.gridSize + 3,self.screen_height - 10))
                    
@dataclass             # shouldnt be a dataclass   
class smokeTrail:
    width : int = 3
    color : tuple[int] = (124,252,0) # green
    
    def __post_init__(self) -> None:
        self.points = []
        
    def addPoint(self,position,randDomness = 0):
        if randDomness != 0:
            randDomness = random.randint(-randDomness,randDomness)
            
        self.points.append((position[0] + randDomness,position[1] + randDomness, self.width,self.width))
        
    
    def draw(self,screen,pos = None,rand = None):
        
        if pos is not None and rand is not None:
            self.addPoint(pos,rand)
        
        for point in self.points:
            draw.rect(screen,
                        self.color,
                        point,)
        
        