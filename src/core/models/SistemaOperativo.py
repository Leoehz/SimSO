from core.models.Ejecutable import Ejecutable
from core.models.Proceso import Proceso
from core.models.Procesador import Procesador
from core.models.Estado import Estado

class SistemaOperativo:
    def __init__(self, ejecutables: Ejecutable, procesador: Procesador):
        self.procesos = [Proceso(ejecutable) for ejecutable in ejecutables]
        self.procesador = procesador
        self.rafagaInstrucciones = 3
        self.cantInstrucciones = 1
        self.procesoActivo = 0
        self.finEjecucion = False

        self.procesador.ejecutarProceso(self.procesos[self.procesoActivo])

    def buscarSiguienteProceso(self):
        encontre_siguiente = False
        while not encontre_siguiente:
            self.procesoActivo = (self.procesoActivo+1) % len(self.procesos) 
            if(self.procesos[self.procesoActivo].estado == Estado.BLOQUEADO):
                encontre_siguiente = True
        self.procesador.ejecutarProceso(self.procesos[self.procesoActivo])
        self.cantInstrucciones = 0

    # Mientras haya instrucciones segui ejecutando    
    def clockHandler(self):

        if self.finEjecucion:
            return True

        proceso = self.procesador.getProceso()

        if self.procesador.procesoTerminado():
            proceso.setEstado(Estado.FINALIZADO)

            if all([p.getEstado() == Estado.FINALIZADO for p in self.procesos]):
                self.finEjecucion = True
                return True
            else:
                self.buscarSiguienteProceso()

        elif (self.cantInstrucciones == self.rafagaInstrucciones):
            proceso.setEstado(Estado.BLOQUEADO)
            self.procesador.detenerProcesoActual()
            self.buscarSiguienteProceso()
            
        self.cantInstrucciones += 1
        return False


    def sysCallHandler(self, servicio, params):
        if (servicio == 1):
            valor = params[0]
            fila = params[1]
            columna = params[2]
            self.procesos[self.procesoActivo].setDataMemoriaVideo(fila, columna, valor)