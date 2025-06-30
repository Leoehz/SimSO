from core.models.Ejecutable import Ejecutable
from core.models.Registro import Registro as R
from core.models.Estado import Estado
import numpy as np

class Proceso:
    def __init__(self, ejecutable: Ejecutable):
        self.ejecutable = ejecutable
        self.stack = []
        self.contexto = {  R.AX: 0,
                            R.BX: 0,
                            R.CX: 0,
                            R.DX: 0,
                            R.IP: ejecutable.getEntryPoint(),
                            R.FLAG: 0,
                            R.CARRY_FLAG: 0
                        }
        self.estado = Estado.BLOQUEADO
        self.matrizVideo = np.zeros((10, 10), int)

    # Mientras haya instrucciones segui ejecutando    
    def getEjecutable(self):
        return self.ejecutable

    def pushValorStack(self, value):
        self.stack.append(value)

    def popValorStack(self):
        return self.stack.pop()

    def guardarContexto(self, registros: R):
        self.contexto = registros.copy()

    def obtenerContexto(self):
        return self.contexto

    def getEstado(self):
        return self.estado

    def setEstado(self, estado: Estado):
        self.estado = estado

    def setDataMemoriaVideo(self, fila, columna, valor):
        self.matrizVideo[fila][columna] = valor

    def getMemoriaVideo(self):
        return self.matrizVideo

    def getStack(self):
        return self.stack