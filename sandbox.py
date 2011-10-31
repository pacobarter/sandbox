# -- coding: utf-8 --
# =============================================================================
#                                                                            
#   Filename.py                                                              
#   (c) 2011 rjimenez                                                        
#                                                                            
#   Description                                                              
#                                                                            
# ============================================================================= 

import pygame
import pygame.locals

SANDBOX_CONTINUE    = True
SANDBOX_TERMINATE   = False

MOUSE_BTN_LEFT      = 1
MOUSE_BTN_MIDDLE    = 2
MOUSE_BTN_RIGHT     = 3

# =============================================================================
#    clase SandBoxWndDelegate, en quien delega SandBoxWnd para las operaciones 
#    'estandar' y que servira de clase base
#
class SandBoxWndDelegate:
    def __init__(self):
        pass

    def fn_init(self, screen):
        pass
    
    def fn_frame_updater(self, screen, clock, tick_time):
        pass
    
    def fn_event_manager(self, lst_event):
        return SANDBOX_CONTINUE

# =============================================================================
#    clase SandBoxWnd (dibuja en pantalla y gestiona eventos)
#
class SandBoxWnd:
    version = (pygame.ver, '0.1')

    #
    #   CTOR
    #
    def __init__(self, w, h, caption, fps, delegate):
        pygame.init() 

        self.screen = pygame.display.set_mode((w,h), pygame.locals.DOUBLEBUF)
        pygame.display.set_caption(caption)

        self.mainloop = True
        
        self.fps = fps
        self.clock = pygame.time.Clock()

        if delegate == None:
            raise Exception('Delegate object cannot be null')

        self.delegate = delegate
        
        self.delegate.fn_init(self.screen)
    
        
    #
    #   MAIN LOOP
    #
    def loop(self):
        try:
            # bucle ppal
            while self.mainloop:
                if not self.delegate:
                    break
                
                # actualizamos el tiempo
                tick_time = self.clock.tick(self.fps) # milliseconds since last frame

                # gestion de eventos
                lst_evt = pygame.event.get()
                self.mainloop = self.delegate.fn_event_manager(lst_evt)

                # actualizacion del frame
                self.delegate.fn_frame_updater(self.screen, self.clock, tick_time)

                # update del display
                pygame.display.update()
        
        finally:
            pygame.quit()        

