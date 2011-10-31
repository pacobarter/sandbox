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
        self.pto   = objects.Point(x,y)
        self.angle = angle
        
        self.d = 15.0
        self.rad = 3.0
        self.color = (0,50,200)
    
        self.move = False
        
        self.target = None
    
    def update(self, screen, clock, tick_time):
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

    def draw(self, surface):
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
class MyDelegate(sandbox.SandBoxWndDelegate):
    def __init__(self):
        self.color      = (132,32,32)
        self.back_color = (25,25,25)

        self.update = False

        self.target = objects.Target(200,300)

        self.agent  = MyAgent(400,100,math.pi/6.0)
        self.agent.set_target(self.target)
        
        self.track = objects.Track()
        self.track.add_point(self.agent.pto)

    def fn_init(self, screen):
        self.bg = pygame.Surface(screen.get_size())
        self.bg = self.bg.convert()
    
    def fn_frame_updater(self, screen, clock, tick_time):
        #   update del status
        #
        if self.update:
            self.agent.update(screen, clock, tick_time)
            self.track.add_point(self.agent.pto)
        
        #   redraw de los objetos
        #
        self.bg.fill(self.back_color)
    
        self.target.draw(self.bg)
        self.agent.draw(self.bg)
        self.track.draw(self.bg)
    
        #   actualizacion del screen
        #
        screen.blit(self.bg,(0,0))
    
    def fn_event_manager(self, lst_event):
        ret = sandbox.SANDBOX_CONTINUE
    
        for event in lst_event:
            if event.type == pygame.QUIT:
                ret = sandbox.SANDBOX_TERMINATE
            
            elif event.type == pygame.KEYDOWN:
                ret = self.manage_key_down(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ret = self.manage_mouse_btn_down(event)
            
        return ret

    #       event MOUSE_BTN_DOWN
    #
    def manage_mouse_btn_down(self, event):
        if event.button == sandbox.MOUSE_BTN_LEFT:
            self.target.set_pos(event.pos)
        
        return sandbox.SANDBOX_CONTINUE



    #       event KEY DOWN
    #
    def manage_key_down(self, event):
        ret = sandbox.SANDBOX_CONTINUE
    
        if event.key == pygame.K_ESCAPE:
            ret = sandbox.SANDBOX_TERMINATE
            
        elif event.key == pygame.K_SPACE:
            self.update = True
        
        return ret


# =============================================================================
#
#
def main():
    sb = sandbox.SandBoxWnd(800, 600, 'Testing new idea', 30, MyDelegate())
    sb.loop()

if __name__ == '__main__':
    main()