from ..models.Registro import Registro as R
from ..models.Ejecutable import Ejecutable
from ..models.Visualizador import Visualizador
import time

class Procesador:
    def __init__(self):
        self.Registros = {R.AX: 0,
                          R.BX: 0,
                          R.CX: 0,
                          R.DX: 0,
                          R.IP: 0,
                          R.FLAG: 0}
        self.lookup_table = {}

    # Mientras haya instrucciones segui ejecutando    
    def ejecutar(self, ejecutable: Ejecutable):
        cantInstrucciones = len(ejecutable.getInstrucciones())
        self.lookup_table = ejecutable.getLookupTable()
        self.setRegister(R.IP, ejecutable.getEntryPoint())
        while(self.getIP() < cantInstrucciones):
            ejecutable.getInstruccion(self.Registros[R.IP]).ejecutar(self)
            Visualizador().mostrar(ejecutable=ejecutable, registros=self.Registros)
            self.incrementarIP()
            time.sleep(1)

    
    def getLookupTable(self):
        return self.lookup_table

    def incrementarIP(self):
        self.Registros[R.IP] += 1

    def setRegister(self, registro: R, value):
        self.Registros[registro] = value

    def getRegister(self, registro: R):
        return self.Registros[registro]
    
    def getIP(self):
        return self.getRegister(R.IP)