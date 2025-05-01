from ..models.Registro import Registro as R
from ..models.Ejecutable import Ejecutable
from interfaces.Instruccion import Instruccion
from time import time
# TODO: Terminar de implementar lo siguiente en el procesador:
# ax, bx, cx, dx - Registros de proposito general
# IP - Instruction Pointer
# Flag

class Procesador:

    def __init__(self, IP: int):
        self.IP = IP
        self.Registros = {R.AX: 0,
                          R.BX: 0,
                          R.CX: 0,
                          R.DX: 0}

    # Mientras haya instrucciones segui ejecutando
    def procesar(self, Ejecutable: ejecutable):
        self.ejecutar(ejecutable)
    
    def ejecutar(Ejecutable: ejecutable):
        cantInstrucciones = len(ejecutable.getInstrucciones())
        while(self.getIP < cantInstrucciones):
            self.Registros = ejecutable.getInstruccion(self.IP).ejecutar(self.Registros)
            self.incrementarIP()
            time.sleep(2)


    def getIP(self):
        return self.IP

    def incrementarIP(self):
        self.IP += 1

    def setRegister(self, Registro: registro, value):
        self.Registros[registro] = value

    def getRegister(self, Registro: registro):
        return self.Registros[registro]