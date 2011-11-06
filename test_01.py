'''
Created on 31/10/2011

@author: raul
'''
import math
import pygame
import sandbox
import agent
import objects

# =============================================================================
#   clase Agente de ejemplo
#
class MyAgent(agent.Agent):
    def __init__(self, pos, angle):
        agent.Agent.__init__(self, agent.AgentDrawer2D(pos, angle))
        
        self.target = None
        self.move = False
        
    def set_target(self, target):
        self.target = target

    def set_move(self, move):
        self.move = move

    def update(self, screen, clock, tick_time):
        if self.target:
            x, y = self.drawer.get_pos()
            
            xf = self.target.get_x()
            yf = self.target.get_y()
            
            self.drawer.set_angle(math.atan2(yf - y, xf - x))
            
            dx = (x - xf)**2
            dy = (y - yf)**2
            
            if math.sqrt(dx+dy)<1:
                self.set_move(False)
            
            else:
                self.set_move(True)
            
            if self.move:
                self.drawer.set_x(0.8 * x + 0.2 * xf)
                self.drawer.set_y(0.8 * y + 0.2 * yf)
                

# =============================================================================
#
#
class MyDelegate(sandbox.DefaultSandBoxWndDelegate):
    def __init__(self):
        sandbox.DefaultSandBoxWndDelegate.__init__(self)
        
        self.update = False

        self.target = objects.Target([200,300])

        self.agent  = MyAgent([400,100], math.pi/6.0)
        self.agent.set_target(self.target)
        
        self.track = objects.Track()
        self.track.add_point(self.agent.drawer.get_pos())
        
        self.add_object(self.agent)
        self.add_object(self.target)
        self.add_object(self.track)
        
    def fn_needs_update(self):
        return self.update

    def fn_logic_updater(self, clock, tick_time):
        sandbox.DefaultSandBoxWndDelegate.fn_logic_updater(self, clock, tick_time)
        
        self.track.add_point(self.agent.drawer.get_pos())

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