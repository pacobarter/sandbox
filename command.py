# -*- coding: utf-8 -*-
#
'''
Created on 06/11/2011

@author: raul
'''

class Command:
    '''
    Encapsula un comando enviado a un objeto
    '''

    def __init__(self, cmd_method, cmd_params):
        '''
        @param cmd_method metodo que sera llamado al ejecutar este comando
        @param cmd_params parametros que se le pasaran al metodo cuando este se ejecute 
        '''
        self.cmd_method = cmd_method
        self.cmd_params = cmd_params  
        
    def execute(self):
        return self.cmd_method(*self.cmd_params)



if __name__ == '__main__':
        class A:
            def __init__(self):
                self.a = 10
                
            def metodo(self,b,c):
                print 'a =', self.a
                print 'b =', b
                print 'c =', c
        
        ta = A()
        cmd = Command(ta.metodo, (20,30))
        cmd.execute()

