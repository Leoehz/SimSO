from Ensamblador import Ensamblador

class Ejecutable:
    def __init__(self, path):
        self.ensamblador = Ensamblador(path)

    def crearEjecutable(self):
        self.instrucciones, self.error = self.ensamblador.parsear()
        if self.error[0]:
            print(self.error[1])
            raise Exception

    def ejecutar(self):
        for instruccion in self.instrucciones:
            instruccion.ejecutar()