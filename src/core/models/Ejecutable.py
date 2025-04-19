from Ensamblador import *

class Ejecutable:
    def __init__(self, path):
        self.ensamblador = Ensamblador(path)

    def crearEjecutable(self):
        self.instrucciones, self.error = self.ensamblador.parsear()
        if self.error[0]:
            print(error[1])
            raise Exception

    def ejecutar(self):
        for instruccion in instrucciones:
            instruccion.ejecutar()