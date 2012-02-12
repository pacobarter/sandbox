# -*- coding: utf-8 -*-
#
'''
Created on 25/12/2011

@author: raul
'''
import pygame
import math

import pgwnd

class Agent:
    def __init__(self, x,y):
        self.pos = [x,y]
        self.vel = [0, 0]
        self.acc = [0, 0]

        self.vel_max = 0.1
        
        self.color = (200, 0, 0)
        
    def update(self, wnd, tick_time):
        self.vel[0] += self.acc[0] * tick_time
        self.vel[1] += self.acc[1] * tick_time
        
        v = math.sqrt(self.vel[0]**2 + self.vel[1]**2)
        if v > 0:
            self.vel[0] = (self.vel[0] * self.vel_max) / v
            self.vel[1] = (self.vel[1] * self.vel_max) / v
        
        self.pos[0] += self.vel[0] * tick_time 
        self.pos[1] += self.vel[1] * tick_time 

        if self.pos[0] > wnd.width or self.pos[0] < 0:
            self.vel[0] = -self.vel[0]

        if self.pos[1] > wnd.height or self.pos[1] < 0:
            self.vel[1] = -self.vel[1]

    def draw(self, wnd, surface, tick_time):
        p1 = (int(self.pos[0]), int(self.pos[1]))
        p2 = (int(self.vel[0] + self.pos[0]), int(self.vel[1] + self.pos[1]))

        pygame.draw.line(surface, self.color, p1, p2)
        pygame.draw.circle(surface, self.color, p1, 5)


class Manager:
    def __init__(self):
        self.bg = None
        self.back_color = (25,25,25)
        
        self.agent = Agent(10,10)
        
        self.target = Agent(10,10)
        self.target.color = (0, 200, 0)

    def fn_init(self, wnd):
        self.bg = pygame.Surface(wnd.screen.get_size())
        self.bg = self.bg.convert()

    def fn_update(self, wnd, tick_time):
        self.agent.update(wnd, tick_time)
        
        v = (self.target.pos[0] - self.agent.pos[0], self.target.pos[1] - self.agent.pos[1])
        mv = math.sqrt(v[0]**2 + v[1]**2)
        
        if mv < 2:
            self.agent.acc = [0,0]
            self.agent.vel = [0,0]

        elif mv < 50:
            self.agent.acc = [0,0]
            
            self.agent.vel[0] /= 2
            self.agent.vel[1] /= 2

    def fn_draw(self, wnd, tick_time):
        self.bg.fill(self.back_color)
    
        self.agent.draw(wnd, self.bg, tick_time)
        self.target.draw(wnd, self.bg, tick_time)
    
        wnd.screen.blit(self.bg, (0,0))

    def fn_evt_mouse_btn_up(self, wnd, evt):
        self.target.pos[0] = evt.pos[0]
        self.target.pos[1] = evt.pos[1]
        
        direc = (self.target.pos[0] - self.agent.pos[0], self.target.pos[1] - self.agent.pos[1])
        mdir = math.sqrt(direc[0]**2 + direc[1]**2)
        
        if mdir > 10:
            self.agent.acc[0] = direc[0]/mdir
            self.agent.acc[1] = direc[1]/mdir
        
        
#
#    --- MAIN ---
#
if __name__ == '__main__':
    wnd = pgwnd.PGWindow('Test PGWindow', (800,600), 30)
    
    mngr = Manager()
    
    wnd.setHandlerInit(mngr.fn_init)
    wnd.setHandlerUpdate(mngr.fn_update)
    wnd.setHandlerDraw(mngr.fn_draw)
    wnd.setHandlerEvent(pygame.MOUSEBUTTONUP, mngr.fn_evt_mouse_btn_up)
    
    wnd.run()