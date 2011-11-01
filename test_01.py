'''
Created on 31/10/2011

@author: raul
'''
import math
import pygame
import sandbox
from agent import Agent
import objects

# =============================================================================
#   clase Agente
#
class MyAgent(Agent):
    def __init__(self, x,y, angle):
        Agent.__init__(self)
        
        self.pto   = objects.Point(x,y)
        self.angle = angle
        
        self.d = 15.0
        self.rad = 3.0
        self.color = (0,50,200)
    
        self.move = False
        
        self.target = None
    
    def update(self, screen, clock, tick_time):
        Agent.update(self, screen, clock, tick_time)
        
        if self.target:
            xf = self.target.x
            yf = self.target.y
            
            self.angle = math.atan2(yf-self.pto.y, xf-self.pto.x)
            
            dx = (self.pto.x-xf)**2
            dy = (self.pto.y-yf)**2
            
            if math.sqrt(dx+dy)<1:
                self.set_move(False)
            
            else:
                self.set_move(True)
            
            if self.move:
                self.pto.x = 0.8*self.pto.x + 0.2 * xf
                self.pto.y = 0.8*self.pto.y + 0.2 * yf

    def draw(self, surface, clock, tick_time):
        Agent.draw(self, surface, clock, tick_time)
        
        p1=(int(self.pto.x), int(self.pto.y))
        p2=(int(self.pto.x + self.d*math.cos(self.angle)), int(self.pto.y + self.d*math.sin(self.angle)))
        
        pygame.draw.line(surface, self.color,p1,p2)
        pygame.draw.circle(surface, self.color, p1, int(self.rad))
    
    def set_target(self, target):
        self.target =  target
        
    def set_move(self, move):
        self.move = move

    

# =============================================================================
#
#
class MyDelegate(sandbox.DefaultSandBoxWndDelegate):
    def __init__(self):
        sandbox.DefaultSandBoxWndDelegate.__init__(self)
        
        self.update = False

        self.target = objects.Target(200,300)

        self.agent  = MyAgent(400,100,math.pi/6.0)
        self.agent.set_target(self.target)
        
        self.track = objects.Track()
        self.track.add_point(self.agent.pto)
        
        self.add_object(self.agent)
        self.add_object(self.target)
        self.add_object(self.track)
        
    def fn_needs_update(self):
        return self.update

    def fn_logic_updater(self, clock, tick_time):
        sandbox.DefaultSandBoxWndDelegate.fn_logic_updater(self, clock, tick_time)
        
        self.track.add_point(self.agent.pto)

    def fn_mouse_event(self, id_button, is_down, pos):
#        if is_down and id_button == sandbox.MOUSE_BTN_LEFT:
#            self.target.set_pos(pos)
        
        return sandbox.SANDBOX_CONTINUE

    def fn_mouse_motion_event(self, pos, rel, buttons):
        if sandbox.MOUSE_BTN_LEFT in buttons:
            self.target.set_pos(pos)
        
        return sandbox.SANDBOX_CONTINUE

    def fn_keyb_event(self, key, is_down):
        ret = sandbox.SANDBOX_CONTINUE
    
        if is_down:
            if key == pygame.K_ESCAPE:
                ret = sandbox.SANDBOX_TERMINATE
                
            elif key == pygame.K_SPACE:
                self.update = True
        
        return ret

    def fn_default_event_handler(self, event):
        return sandbox.SANDBOX_CONTINUE


# =============================================================================
#
#
def main():
    sb = sandbox.SandBoxWnd(800, 600, 'Testing new idea', 30, MyDelegate())
    sb.loop()

if __name__ == '__main__':
    main()