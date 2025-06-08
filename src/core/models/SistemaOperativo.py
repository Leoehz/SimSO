from core.models.Ejecutable import Ejecutable
from core.models.Proceso import Proceso
from core.models.Procesador import Procesador
from core.models.Estado import Estado

class SistemaOperativo:
    def __init__(self, ejecutables: Ejecutable, procesador: Procesador):
        self.procesos = []
        self.procesador = procesador
        self.rafagaInstrucciones = 3
        self.cantInstrucciones = 1
        self.procesoActivo = 0
        for ejecutable in ejecutables:
            self.procesos.append(Proceso(ejecutable))
        self.procesador.ejecutarProceso(self.procesos[self.procesoActivo])

    # Mientras haya instrucciones segui ejecutando    
    def clockHandler(self, esInstruccion):
        if (self.cantInstrucciones == self.rafagaInstrucciones or self.procesador.procesoTerminado()):
            if (self.procesador.procesoTerminado()):
                self.procesador.getProceso().setEstado(Estado.FINALIZADO)
            else:
                self.procesador.getProceso().setEstado(Estado.BLOQUEADO)

            self.procesador.detenerProcesoActual()
            
            encontre = False
            while (not encontre):
                self.procesoActivo = (self.procesoActivo+1) % len(self.procesos) 
                if(self.procesos[self.procesoActivo].estado == Estado.BLOQUEADO):
                    encontre = True
                    #print(self.procesoActivo)
            if(encontre):
                self.procesador.ejecutarProceso(self.procesos[self.procesoActivo])
                self.cantInstrucciones = 0
            else:
                self.procesador.setEstado(Estado.INACTIVO)
            
                
        else:
            pass
        if(esInstruccion):
            self.cantInstrucciones+=1


