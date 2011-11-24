# -*- coding: utf-8 -*-
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
    
    def fn_needs_update(self):
        return True
    
    def fn_logic_updater(self, clock, tick_time):
        pass
    
    def fn_frame_draw(self, clock, tick_time):
        pass

    def fn_event_manager(self, lst_event):
        return SANDBOX_CONTINUE

# =============================================================================
#    clase DefaultSandBoxWndDelegate, tiene lista de objetos updatables/drawables
#    y gestion basica de eventos
#
class DefaultSandBoxWndDelegate(SandBoxWndDelegate):
    def __init__(self):
        SandBoxWndDelegate.__init__(self)
        
        self.lst_objects = []
        self.back_color = (25,25,25)

    def add_object(self, obj):
        if obj:
            self.lst_objects.append(obj)

    def fn_init(self, screen):
        self.screen = screen
        self.bg = pygame.Surface(screen.get_size())
        self.bg = self.bg.convert()
    
    def fn_logic_updater(self, clock, tick_time):
        for obj in self.lst_objects:
            obj.update(self.screen, clock, tick_time)
    
    def fn_frame_draw(self, clock, tick_time):
        # pintamos el background
        #
        self.bg.fill(self.back_color)

        # redraw de los objetos
        #
        for obj in self.lst_objects:
            obj.draw(self.bg, clock, tick_time)

        # actualizacion del screen
        #
        self.screen.blit(self.bg, (0,0))

    
    def fn_event_manager(self, lst_event):
        ret = SANDBOX_CONTINUE
    
        for event in lst_event:
            if event.type == pygame.QUIT:
                ret = SANDBOX_TERMINATE
            
            elif event.type == pygame.KEYDOWN:
                ret = self.fn_keyb_event(event.key, True)
                
            elif event.type == pygame.KEYUP:
                ret = self.fn_keyb_event(event.key, False)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ret = self.fn_mouse_event(event.button, True, event.pos)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                ret = self.fn_mouse_event(event.button, False, event.pos)

            elif event.type == pygame.MOUSEMOTION:
                ret = self.fn_mouse_motion_event(event.pos, event.rel, event.buttons)

            else:
                ret = self.fn_default_event_handler(event)
            
        return ret

    def fn_mouse_event(self, id_button, is_down, pos):
        return SANDBOX_CONTINUE

    def fn_mouse_motion_event(self, pos, rel, buttons):
        return SANDBOX_CONTINUE

    def fn_keyb_event(self, key, is_down):
        return SANDBOX_CONTINUE

    def fn_default_event_handler(self, event):
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
        
    #
    #   MAIN LOOP
    #
    def loop(self):
        try:
            if not self.delegate:
                raise Exception('No se ha indicado un Delegate valido')

            # inicializacion
            self.delegate.fn_init(self.screen)

            # bucle ppal
            while self.mainloop:
                
                # actualizamos el tiempo
                tick_time = self.clock.tick(self.fps) # milliseconds since last frame

                # gestion de eventos
                lst_evt = pygame.event.get()
                self.mainloop = self.delegate.fn_event_manager(lst_evt)

                # actualizacion de la logica 
                if self.delegate.fn_needs_update():
                    self.delegate.fn_logic_updater(self.clock, tick_time)

                self.delegate.fn_frame_draw(self.clock, tick_time)

                # update del display
                pygame.display.update()
        
        finally:
            pygame.quit()        

