from core.models.Registro import Registro as R
from core.models.Ejecutable import Ejecutable

import time

# TODO: PASAR EJECUTABLE A INSTRUCCIONES

class Proceso:
    def __init__(self, ejecutable: Ejecutable):
        self.ejecutable = ejecutable
        self.stack = []

    # Mientras haya instrucciones segui ejecutando    
    def getEjecutable(self):
        return self.ejecutable

    def pushValorStack(self, value):
        self.stack.append(value)

    def popValorStack(self):
        return self.stack.pop()