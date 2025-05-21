from interfaces.Instruccion import Instruccion
from core.models.Registro import Registro

class Cmp(Instruccion):
    N_PARAMS = 2
    SYNTAX = 'cmp'
    PARAMS_TYPE = [(Registro, int), (Registro, int)]

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __repr__(self):
        return f'Cmp({self.param1})'

    def ejecutar(self, procesador, ejecutable):
        dummy = self.param2
        flag = 0
        if(type(dummy) == Registro):
            flag = procesador.getRegister(dummy) == procesador.getRegister(self.param1)
        else:
            if(type(self.param1) == Registro):
                flag = procesador.getRegister(self.param1) == dummy
            else:
                flag = self.param1 == self.param2
        procesador.setRegister(Registro.FLAG, flag)
        return