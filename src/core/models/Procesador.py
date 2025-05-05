from ..models.Registro import Registro as R
from ..models.Ejecutable import Ejecutable
from ..models.Visualizador import Visualizador
import time
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
                          R.DX: 0,
                          R.IP: IP,
                          R.FLAG: 0}

    # Mientras haya instrucciones segui ejecutando
    def procesar(self, ejecutable: Ejecutable):
        self.ejecutar(ejecutable)
    
    def ejecutar(self, ejecutable: Ejecutable):
        cantInstrucciones = len(ejecutable.getInstrucciones())
        while(self.getIP() < cantInstrucciones):
            Visualizador().mostrar(ejecutable=ejecutable, IP=self.getIP())
            self.Registros = ejecutable.getInstruccion(self.IP).ejecutar(self.Registros)
            self.incrementarIP()
            time.sleep(1)


    def getIP(self):
        return self.IP

    def incrementarIP(self):
        self.IP += 1

    def setRegister(self, registro: R, value):
        self.Registros[registro] = value

    def getRegister(self, registro: R):
        return self.Registros[registro]