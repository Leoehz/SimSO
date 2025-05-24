from interfaces.Instruccion import Instruccion
from ..Registro import Registro

class Ret(Instruccion):
    N_PARAMS = 0
    SYNTAX = 'ret'
    PARAMS_TYPE = []

    def __init__(self):
        pass

    def __repr__(self):
        return f'Ret()'

    def ejecutar(self, procesador, ejecutable):
        proceso = procesador.getProceso()
        dummy = proceso.popValorStack()
        procesador.setRegister(Registro.IP, dummy)
        return