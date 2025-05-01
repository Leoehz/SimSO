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

    def ejecutar(self, registros):
        dummy = self.param2
        if(type(dummy)==Registro):
            dummy = registros[self.param2]

        registros[self.param1] = dummy
        self.param1 = self.param2
        return registros
        #return self.param1