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

    def ejecutar(self, procesador):
        lookup_table = procesador.getProceso().getEjecutable().getLookupTable()
        proceso = procesador.getProceso()
        registro = Registro.IP
        valor = procesador.getRegister(registro)
        procesador.setPreservadorIP(valor)
        proceso.pushValorStack(valor)
        procesador.setRegister(registro, lookup_table[self.param1])
        return