from interfaces.Instruccion import Instruccion
from core.models.Registro import Registro

class Inc(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'inc'
    PARAMS_TYPE = [(Registro, int)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Inc({self.param1})'

    def ejecutar(self, procesador, ejecutable):   
        dummy = self.param1
        if(type(dummy)==Registro):
            dummy = procesador.getRegister(self.param1) + 1
            procesador.setRegister(self.param1, dummy)       
        else:
            dummy += 1   
        return