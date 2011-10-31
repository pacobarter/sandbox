'''
Created on 31/10/2011

@author: raul
'''

import objects

# =============================================================================
#    Base class for Agent definition
#
class Agent(objects.Drawable):
    '''
    Base class for Agent definition
    '''

    def __init__(self):
        pass
    
    def update(self, screen, clock, tick_time):
        pass
    
    def draw(self, surface):
        pass
    
