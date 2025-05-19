from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Jnz(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'jmz'
    PARAMS_TYPE = [(str,)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Jmz({self.param1})'

    def ejecutar(self, procesador, ejecutable):
        if procesador.getRegister(Registro.FLAG) == 1:
            lookup_table = procesador.getLookupTable()
            procesador.setRegister(Registro.IP, lookup_table[self.param1]-1)
        return