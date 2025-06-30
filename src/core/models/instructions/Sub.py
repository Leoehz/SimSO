from interfaces.Instruccion import Instruccion
from core.models.Registro import Registro

class Sub(Instruccion):
    N_PARAMS = 2
    SYNTAX = 'sub'
    PARAMS_TYPE = [(Registro, int), (Registro, int)]

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __repr__(self):
        return f'Sub({self.param1}, {self.param2})'

    def ejecutar(self, procesador):
        dummy = self.param2
        if(type(dummy)==Registro):
            dummy = procesador.getRegister(self.param1) - procesador.getRegister(self.param2)
        else:
            if(type(self.param1) == Registro):
                dummy = procesador.getRegister(self.param1) - dummy

        if(type(self.param1) == Registro):
            procesador.setRegister(self.param1, dummy)
        procesador.incrementarIP()
        return
