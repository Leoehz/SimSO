from interfaces.Instruccion import Instruccion

class Dec(Instruccion):
    def __init__(self, param1):
        self.param1 = param1

    def ejecutar(self):
        self.param1 -= 1
        return self.param1