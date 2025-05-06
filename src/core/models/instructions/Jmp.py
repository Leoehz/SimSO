from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Jmp(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'jmp'
    PARAMS_TYPE = [(str,)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Jmp({self.param1})'

    def ejecutar(self, procesador):
        lookup_table = procesador.getLookupTable()
        procesador.setRegister(Registro.IP, lookup_table[self.param1]-1)
        return