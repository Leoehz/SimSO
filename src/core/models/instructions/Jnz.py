from interfaces.Instruccion import Instruccion
from core.models.Registro import Registro

class Jnz(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'jnz'
    PARAMS_TYPE = [(str,)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Jnz("{self.param1}")'

    def ejecutar(self, procesador):
        if procesador.getRegister(Registro.FLAG) == 1:
            ejecutable = procesador.getProceso().getEjecutable()
            lookup_table = ejecutable.getLookupTable()
            procesador.setRegister(Registro.IP, lookup_table[self.param1])
        procesador.incrementarIP()
        return