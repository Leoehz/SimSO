from .Ejecutable import Ejecutable

class Visualizador:
    def __init__(self):
        pass

    def mostrar(self, ejecutable: Ejecutable, IP: int):
        listadoInstrucciones = ejecutable.getInstrucciones() # [1,2,3,4,5,6] # [1, 2, 3] # [1, 2, 3, 4]
        chunk = 2

        visibleChunk = listadoInstrucciones[max(IP-chunk, 0):min(IP+chunk, len(listadoInstrucciones))] # [1,2,3,4,5]
        # [1,2,3]
        printableInstructions = [f'\t{instruction}' for instruction in visibleChunk]

        if IP < chunk:
            printable_IP = 0
        elif IP > len(listadoInstrucciones) - chunk:
            printable_IP = -1
        else:
            printable_IP = chunk

        printableInstructions[printable_IP] = f'>{printableInstructions[printable_IP]}'

        printable = f"\n\n=== Paso siguiente ===\n\n{'\n'.join(printableInstructions)}"

        print(printable) 