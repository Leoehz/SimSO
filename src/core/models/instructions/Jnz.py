from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Jnz(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'jmz'
    PARAMS_TYPE = [str]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Jmz({self.param1})'

    def ejecutar(self):
        pass