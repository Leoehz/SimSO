from interfaces.Instruccion import Instruccion

class Add(Instruccion):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def ejecutar(self):
        self.param1 += self.param2
        return self.param1