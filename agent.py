'''
Created on 31/10/2011

@author: raul
'''

import pygame
import math
import objects

# =============================================================================
#    Base class for Agent definition
#
class Agent(objects.Entity):
    '''
    Base class for Agent definition
    '''
    def __init__(self, drawer):
        objects.Entity.__init__(self)
        
        self.drawer = drawer
    
    def update(self, screen, clock, tick_time):
        pass
    
    def draw(self, surface, clock, tick_time):
        self.drawer.draw(self, surface, clock, tick_time)


# =============================================================================
#    Default Agent 2D Drawer definition
#
class AgentDrawer2D(objects.Entity2D):
    def __init__(self, pos = [0,0], angle = 0):
        objects.Entity2D.__init__(self, pos, angle)
        
        self.d = 15.0
        self.rad = 3.0
        self.line_color = (0, 200, 0)
        self.circle_color = (10, 150, 150)

    def draw(self, agent, surface, clock, tick_time):
        x = self.get_x()
        y = self.get_y()
        
        p1 = (int(x), int(y))
        p2 = (int(x + self.d * math.cos(self.angle)), int(y + self.d * math.sin(self.angle)))
        
        pygame.draw.line(surface, self.line_color, p1,p2)
        pygame.draw.circle(surface, self.circle_color, p1, int(self.rad))


        