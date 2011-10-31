'''
Created on 31/10/2011

@author: raul
'''

import math
import pygame
from objects import Point

# =============================================================================
#    Base class for Agent definition
#
class Agent:
    '''
    Base class for Agent definition
    '''

    def __init__(self):
        pass
    
    def update(self, screen, clock, tick_time):
        pass
    
    def draw(self, surface):
        pass
    
# =============================================================================
#   clase Agente
#
class XYAgent(Agent):
    def __init__(self, x,y, angle):
        self.pto   = Point(x,y)
        self.angle = angle
        
        self.d = 15.0
        self.rad = 3.0
        self.color = (0,50,200)
    
        self.move = False
    
    def update(self, screen, clock, tick_time):
        pass

    def draw(self, surface):
        p1=(self.pto.x, self.pto.y)
        p2=(self.pto.x + self.d*math.cos(self.angle), self.pto.y + self.d*math.sin(self.angle))
        
        pygame.draw.line(surface, self.color,p1,p2)
        pygame.draw.circle(surface, self.color, p1, self.rad)
    
    def set_move(self, move):
        self.move=move

    def swap_move(self):
        self.set_move(not self.move)
    
