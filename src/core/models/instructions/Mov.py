from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Mov(Instruccion):
    N_PARAMS = 2
    SYNTAX = 'mov'
    PARAMS_TYPE = [(Registro,), (Registro, int)]

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def __repr__(self):
        return f'Mov({self.param1}, {self.param2})'

    def ejecutar(self, procesador, ejecutable):
        if(type(self.param2)==Registro):
            value = procesador.getRegister(self.param2)
        else:
            value = self.param2
        procesador.setRegister(registro=self.param1, value=value)
        return