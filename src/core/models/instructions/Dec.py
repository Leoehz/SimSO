from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Dec(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'dec'
    PARAMS_TYPE = [(Registro, int)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Dec({self.param1})'

    def ejecutar(self, procesador):   
        dummy = self.param1
        if(type(dummy)==Registro):
            dummy = procesador.getRegister(self.param1) - 1
            procesador.setRegister(self.param1, dummy)       
        else:
            dummy -= 1   
        return