from core.models.Registro import Registro as R
from core.models.Ejecutable import Ejecutable
from core.models.Visualizador import Visualizador
from core.models.Proceso import Proceso
from core.models.PreservadorIP import PreservadorIP
import time

class Procesador:
    def __init__(self, Registros: dict = {  R.AX: 0,
                                            R.BX: 0,
                                            R.CX: 0,
                                            R.DX: 0,
                                            R.IP: 0,
                                            R.FLAG: 0}
                ):
        self.Registros = Registros
        self.proceso = None

    # Mientras haya instrucciones segui ejecutando    
    def ejecutar(self, proceso: Proceso):
        self.proceso = proceso
        ejecutable = proceso.getEjecutable()
        cantInstrucciones = len(ejecutable.getInstrucciones())
        self.lookup_table = ejecutable.getLookupTable()
        self.setRegister(R.IP, ejecutable.getEntryPoint())
        while(self.getIP() < cantInstrucciones):
            Visualizador(time_sleep=0.25).mostrar(ejecutable=ejecutable, registros=self.Registros, stack=proceso.stack)
            ejecutable.getInstruccion(self.Registros[R.IP]).ejecutar(self)
            self.incrementarIP()
            Visualizador(time_sleep=0.25).mostrar(ejecutable=ejecutable, registros=self.Registros, stack=proceso.stack)
            time.sleep(1)

    def incrementarIP(self):
        self.Registros[R.IP] += 1

    def setRegister(self, registro: R, value):
        self.Registros[registro] = value

    def getRegister(self, registro: R):
        return self.Registros[registro]
    
    def getRegisters(self):
        return self.Registros
    
    def setRegisters(self, Registros):
        self.Registros = Registros
    
    def getIP(self):
        return self.getRegister(R.IP)

    def getProceso(self):
        return self.proceso

    def setPreservadorIP(self, valor):
        self.preservador = PreservadorIP()
        self.preservador.setValorIP(valor)

    def delPreservador(self):
        del self.preservador

    def getPreservadorIP(self):
        return self.preservador