from interfaces.Instruccion import Instruccion

class Noop(Instruccion):
    N_PARAMS = 0
    SYNTAX = 'noop'
    PARAMS_TYPE = None

    def __init__(self, label: str = None):
        self.label = label
        pass
    
    def __repr__(self):
        if self.label is not None:
            return f'{self.label}:'
        else:
            return f'Noop()'


    def ejecutar(self, procesador):
        procesador.incrementarIP()
        return