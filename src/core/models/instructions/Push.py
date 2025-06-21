from interfaces.Instruccion import Instruccion
from ..Registro import Registro
from ..Procesador import Procesador

class Push(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'push'
    PARAMS_TYPE = [(Registro, int)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Push({self.param1})'

    def ejecutar(self, procesador):
        dummy = self.param1
        if(type(dummy)==Registro):
            dummy = procesador.getRegister(self.param1)
        procesador.getProceso().pushValorStack(dummy)
        procesador.incrementarIP()
        return