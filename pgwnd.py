# -*- coding: utf-8 -*-
#
'''
Created on 21/12/2011

@author: raul
'''

import pygame.locals

MOUSE_BTN_LEFT      = 1
MOUSE_BTN_MIDDLE    = 2
MOUSE_BTN_RIGHT     = 3

def fn_default_quit(wnd, event):
    wnd.do_main_loop = False

class PGWindow(object):
    '''
    Pygame window
    '''

    version = (pygame.ver, '0.1')

    def __init__(self, title, size, fps):
        '''
        Build a pygame window
        @param title Title of the window
        @param size Tuple with window size: (width, height)
        @param fps Frames Per Second, parameter passed to pygame
        '''
        self.title  = title
        self.width  = size[0]
        self.height = size[1]
        self.fps    = fps
        
        self.do_main_loop = True

        # prototipo: fn(wnd)
        self.handler_init   = None
        
        # prototipo: fn(wnd, clock_tick_time)
        self.handler_update = None
        
        # prototipo: fn(wnd, clock_tick_time)
        self.handler_draw   = None

        # prototipo: fn(wnd, evt)
        self.handler_evt = {
            pygame.QUIT            : fn_default_quit,
            pygame.KEYDOWN         : None,
            pygame.KEYUP           : None,
            pygame.MOUSEBUTTONDOWN : None,
            pygame.MOUSEBUTTONUP   : None,
            pygame.MOUSEMOTION     : None
        }

        # init Pygame
        pygame.init() 

        # init Screen
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.locals.HWSURFACE | pygame.locals.DOUBLEBUF)
        pygame.display.set_caption(title)

        # init background (main) surface
        self.background = pygame.Surface(self.screen.get_size()).convert()

        # init clock
        self.clock = pygame.time.Clock()


    def _process_events(self, lst_events):
        '''
        Process pygame events
        '''
        for evt in lst_events:
            if evt.type in self.handler_evt:
                fn = self.handler_evt[evt.type] 
                if fn:
                    fn(self, evt)
        
    def setHandlerInit(self, fn_init):
        '''
        Sets handler for initialization
        @param fn_init User defined function to be called before main loop. 
                       Handler prototype: void fun(PGWindow wnd)
        '''
        self.handler_init = fn_init

    def setHandlerUpdate(self, fn_update):
        '''
        Sets handler for game logic update
        @param fn_update User defined function to be called inside main loop to update game logic. 
                         Handler prototype: void fun(PGWindow wnd, long tick_time)
        '''
        self.handler_update = fn_update

    def setHandlerDraw(self, fn_draw):
        '''
        Sets handler for frame draw
        @param fn_draw User defined function to be called inside main loop to draw each frame. 
                       Handler prototype: void fun(PGWindow wnd, long tick_time)
        '''
        self.handler_draw = fn_draw

    def setHandlerEvent(self, evt_type, evt_hndlr):
        '''
        Sets handler for Pygame events.
        @param evt_type Event type, a Pygame constant
        @param evt_handler User defined function to be called in response to the event. 
                           Handler prototype: void fun(PGWindow wnd, pygame.event evt)
        '''
        self.handler_evt[evt_type] = evt_hndlr
        
    def run(self):
        '''
        Main loop
        '''
        try:
            # inicializacion
            if self.handler_init:
                self.handler_init(self)

            # bucle ppal
            while self.do_main_loop:
                
                # actualizamos el tiempo
                tick_time = self.clock.tick(self.fps) # -> milliseconds since last frame

                # gestion de eventos (donde cambiar 'self.do_main_loop' si se quiere salir)
                self._process_events(pygame.event.get())

                # actualizacion de la logica
                if self.handler_update: 
                    self.handler_update(self, tick_time)

                # pintado del frame
                if self.handler_draw:
                    self.handler_draw(self, tick_time)
                    self.screen.blit(self.background, (0,0))

                # update del display
                pygame.display.update()
        
        finally:
            pygame.quit()        

    
    
    