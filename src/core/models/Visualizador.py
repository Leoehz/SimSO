from .Ejecutable import Ejecutable
from .Registro import Registro as R
from termcolor import colored
import colorama
import os
import platform
import time

def clear_console():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux' or system == 'Darwin':
        os.system('clear')
    else:
        print("Sistema Operativo no soportado para limpiar la consola.")

class Visualizador:
    def __init__(self):
        colorama.init()
        pass

    def mostrar(self, ejecutable: Ejecutable, registros: dict):
        listadoInstrucciones = ejecutable.getInstrucciones()

        IP = registros[R.IP]
        chunk = 20
        lower_bound = max(IP-chunk, 0)
        upper_bound = min(IP+chunk, len(listadoInstrucciones)-1)+1

        visibleChunk = listadoInstrucciones[lower_bound:upper_bound]
        printableInstructions = [f'\t{instruction}' for instruction in visibleChunk]

        if IP < chunk:
            printable_IP = IP
        else:
            printable_IP = chunk

        printableInstructions[printable_IP] = colored(f'>{printableInstructions[printable_IP]}', color='green')
        printable_registers = {x.name: value for x, value in registros.items()}

        printable = f"\n\n{colored('=== Paso siguiente ===', color='light_cyan')}\n\n{'\n'.join(printableInstructions)}\n\nRegistros {printable_registers}"

        print(printable)
        time.sleep(2)

        clear_console()