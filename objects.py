# -*- coding: utf-8 -*-
# =============================================================================
#                                                                            
#   objects.py                                                              
#   (c) 2011 rjimenez                                                        
#                                                                            
#   Description                                                              
#                                                                            
# ============================================================================= 

import pygame

class Entity:
    def __init__(self):
        pass
    
    def update(self, screen, clock, tick_time):
        pass
    
    def draw(self, surface, clock, tick_time):
        pass


class Entity2D(Entity):
    def __init__(self, pos = [0,0], angle = 0):
        Entity.__init__(self)
        
        self.pos = pos
        self.angle = angle

    def set_pos(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]

    def set_pos_rel(self, pos_rel):
        self.pos[0] += pos_rel[0]
        self.pos[1] += pos_rel[1]

    def get_pos(self):
        return self.pos[:]

    def set_x(self, x):
        self.pos[0] = x

    def get_x(self):
        return self.pos[0]

    def set_y(self, y):
        self.pos[1] = y

    def get_y(self):
        return self.pos[1]

    def set_angle(self, angle):
        self.angle = angle

    def set_angle_rel(self, angle_rel):
        self.angle += angle_rel

    def get_angle(self):
        return self.angle



# =============================================================================
#   clase Cross
#
class Cross(Entity2D):
    def __init__(self, pos, color):
        Entity2D.__init__(self, pos)

        self.color = color
        self.d = 10

    def draw(self, surface, clock, tick_time):
        x = self.get_x()
        y = self.get_y()
        
        pygame.draw.line(surface, self.color, (x, y - self.d), (x, y + self.d))
        pygame.draw.line(surface, self.color, (x - self.d, y), (x + self.d, y))


# =============================================================================
#   clase Track
#
class Track(Entity2D):
    def __init__(self):
        self.ptos  = []
        self.color = (0,200,0)

    def add_point(self, p):
        self.ptos.append(p)

    def draw(self, surface, clock, tick_time):
        if len(self.ptos)>1:
            pygame.draw.lines(surface, self.color, False, self.ptos)

# =============================================================================
#   clase Target
#
class Target(Cross):
    def __init__(self, pos):
        Cross.__init__(self, pos, (250,0,0))


