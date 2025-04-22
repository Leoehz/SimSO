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

    def ejecutar(self):
        self.param1 = self.param2
        return self.param1