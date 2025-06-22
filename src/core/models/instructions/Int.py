from interfaces.Instruccion import Instruccion
from core.models.Registro import Registro as R
from core.models.Procesador import Procesador
from exceptions import ExecutionError

class Int(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'int'
    PARAMS_TYPE = [(int,)]

    def __init__(self, nroSysCall):
        self.sysCall = nroSysCall

    def __repr__(self):
        return f'Int({self.sysCall})'

    def ejecutar(self, procesador):
        sistema = procesador.getSistemaOperativo()
        if(self.sysCall == 1):
        # en ax vamos a tener el entero que queremos imprimir, en bx tendrá la fila y cx la columna de donde donde quiero que se imprima en la pantalla
            params = [procesador.getRegister(R.AX), procesador.getRegister(R.BX), procesador.getRegister(R.CX)]
            sistema.sysCallHandler(self.sysCall, params)
        else:
            raise ExecutionError(f'Error de ejecución')
        
        procesador.incrementarIP()
