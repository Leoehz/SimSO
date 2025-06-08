from core.models.Ejecutable import Ejecutable
from core.models.Proceso import Proceso
from core.models.Procesador import Procesador
from core.models.Estado import Estado

class SistemaOperativo:
    def __init__(self, ejecutables: Ejecutable, procesador: Procesador):
        self.procesos = []
        self.procesador = procesador
        self.rafagaInstrucciones = 3
        self.cantInstrucciones = 0
        for ejecutable in ejecutables:
            self.procesos.append(Proceso(ejecutable))
        self.procesador.ejecutarProceso(self.procesos[0])

    # Mientras haya instrucciones segui ejecutando    
    def clockHandler(self):
        self.cantInstrucciones+=1
        if (self.cantInstrucciones == self.rafagaInstrucciones or self.procesador.procesoTerminado()):
            if (self.procesador.procesoTerminado()):
                self.procesador.getProceso().setEstado(Estado.FINALIZADO)
            else:
                self.procesador.getProceso().setEstado(Estado.BLOQUEADO)

            # sacar del procesador el proceso actual: guardar en el Contexto del Proceso los valores de los registros
            self.procesador.detenerProcesoActual()
            #cambio de contexto: buscar  el próximo proceso que debe ejecutar
            encontre = False
            procesoActivo = 0
            while (not encontre):
                procesoActivo = (procesoActivo+1) % len(self.procesos) 
                print(procesoActivo)
                if(self.procesos[procesoActivo].estado == Estado.BLOQUEADO):
                    encontre = True
            if(encontre):
            # setear el procesoActivo como el nuevo proceso que debe ejecutar
    # restituimos el Contexto del nuevo proceso en el Procesador
                self.procesador.ejecutarProceso(self.procesos[procesoActivo])
            # inicializamos contadorInstrucciones (contadorInstrucciones = 0)
                self.contadorInstrucciones = 0
            else:
                self.procesador.setEstado(Estado.INACTIVO)
            
                
        else:
            pass


