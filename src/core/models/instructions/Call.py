from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Call(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'call'
    PARAMS_TYPE = [(str,)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Call({self.param1})'

    def ejecutar(self, procesador, ejecutable):
        lookup_table = procesador.getLookupTable()
        proceso = procesador.getProceso()
        proceso.pushValorStack(procesador.getRegister(Registro.IP))
        procesador.setRegister(Registro.IP, lookup_table[self.param1] - 1)
        return