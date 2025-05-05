from interfaces.Instruccion import Instruccion
from ..Registro import Registro
from ..Procesador import Procesador

class Add(Instruccion):
    N_PARAMS = 2
    SYNTAX = 'add'
    PARAMS_TYPE = [(Registro, int), (Registro, int)]

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __repr__(self):
        return f'Add({self.param1}, {self.param2})'

    def ejecutar(self, registros):
        dummy = self.param2
        if(type(dummy)==Registro):
            dummy = registros[self.param2] + registros[self.param1]
        else:
            dummy += registros[self.param1]
        #self.param1 += self.param2
        #procesador.setRegister(self.param1, dummy)
        registros[self.param1] = dummy
        return registros
        #return self.param1
    
    def get_params(self):
        return self.n_params