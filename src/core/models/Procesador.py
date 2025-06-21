from core.models.Registro import Registro as R
from core.models.Ejecutable import Ejecutable
from core.models.Visualizador import Visualizador
from core.models.Proceso import Proceso
from core.models.PreservadorIP import PreservadorIP
from core.models.Estado import Estado
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
        self.estado = Estado.ACTIVO

    # Mientras haya instrucciones segui ejecutando
    def ejecutarProceso(self, proceso: Proceso):
        self.proceso = proceso
        self.Registros = proceso.obtenerContexto()

    def procesar(self):
        while(self.estado == Estado.ACTIVO):
            ejecutable = self.proceso.getEjecutable()
            self.cantInstrucciones = len(ejecutable.getInstrucciones())
            Visualizador(time_sleep=0.2).mostrar(procesador=self)
            ejecutable.getInstruccion(self.Registros[R.IP]).ejecutar(self)
            finEjecucion = self.sistema.clockHandler()

            if finEjecucion:
                self.estado = Estado.INACTIVO
            time.sleep(1)
            

    def procesoTerminado(self):
        return self.getIP() == self.cantInstrucciones

    def detenerProcesoActual(self):
        self.proceso.guardarContexto(self.Registros)

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

    def setSistemaOperativo(self, sistema):
        self.sistema = sistema

    def getSistemaOperativo(self):
        return self.sistema