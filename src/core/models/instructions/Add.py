from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Add(Instruccion):
    N_PARAMS = 2
    SYNTAX = 'add'
    PARAMS_TYPE = [(Registro, int), (Registro, int)]

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __repr__(self):
        return f'Add({self.param1}, {self.param2})'

    def ejecutar(self):
        self.param1 += self.param2
        return self.param1
    
    def get_params(self):
        return self.n_params