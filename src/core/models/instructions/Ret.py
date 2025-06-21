from interfaces.Instruccion import Instruccion
from core.models.Registro import Registro
#from exceptions import IPIntegrityViolation
import time

class Ret(Instruccion):
    N_PARAMS = 0
    SYNTAX = 'ret'
    PARAMS_TYPE = []

    def __init__(self):
        pass

    def __repr__(self):
        return f'Ret()'

    def ejecutar(self, procesador):
        proceso = procesador.getProceso()
        dummy = proceso.popValorStack()
        print(dummy, procesador.getPreservadorIP().getValorIP())
        if(procesador.getPreservadorIP().getValorIP() != dummy):
            #raise IPIntegrityViolation()
            dummy = procesador.getPreservadorIP().getValorIP()
            print(f'Se rompió la integridad del programa y el IP, retomando punto de control...')
            time.sleep(3)
        procesador.setRegister(Registro.IP, dummy)
        procesador.delPreservador()