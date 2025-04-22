from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Inc(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'inc'
    PARAMS_TYPE = [(Registro, int)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Inc({self.param1})'

    def ejecutar(self):
        self.param1 += 1
        return self.param1