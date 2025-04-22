from Registro import Registro as R
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
    def ejecutar(self):
        pass

    def incrementarIP(self):
        self.IP += 1

    def setRegister(self):
        pass

    def getRegister(self):
        pass