# -- coding: utf-8 --
# =============================================================================
#                                                                            
#   objects.py                                                              
#   (c) 2011 rjimenez                                                        
#                                                                            
#   Description                                                              
#                                                                            
# ============================================================================= 

import pygame

class ObjectBase:
    def update(self, screen, clock, tick_time):
        pass
    
    def draw(self, surface, clock, tick_time):
        pass

# =============================================================================
#   clase Point
#
class Point(ObjectBase):
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def set_pos(self, position):
        self.x=position[0]
        self.y=position[1]


# =============================================================================
#   clase Cross
#
class Cross(Point):
    def __init__(self, x,y, color):
        Point.__init__(self, x,y)

        self.color = color
        
        self.d = 10

    def draw(self, surface, clock, tick_time):
        pygame.draw.line(surface, self.color, (self.x, self.y-self.d), (self.x, self.y+self.d))
        pygame.draw.line(surface, self.color, (self.x-self.d, self.y), (self.x+self.d, self.y))


# =============================================================================
#   clase Track
#
class Track(ObjectBase):
    def __init__(self):
        self.ptos  = []
        self.color = (0,200,0)

    def add_point(self, p):
        self.add(p.x,p.y)

    def add(self, x,y):
        self.ptos.append((x,y))

    def draw(self, surface, clock, tick_time):
        if len(self.ptos)>1:
            pygame.draw.lines(surface, self.color, False, self.ptos)

# =============================================================================
#   clase Target
#
class Target(Cross):
    def __init__(self, x,y):
        Cross.__init__(self, x,y, (250,0,0))


