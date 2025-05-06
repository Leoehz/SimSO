from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Cmp(Instruccion):
    N_PARAMS = 2
    SYNTAX = 'cmp'
    PARAMS_TYPE = [(Registro, int), (Registro, int)]

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __repr__(self):
        return f'Cmp({self.param1})'

    def ejecutar(self):
        pass