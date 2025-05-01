from interfaces.Instruccion import Instruccion

class Noop(Instruccion):
    N_PARAMS = 0
    SYNTAX = 'noop'
    PARAMS_TYPE = None

    def __init__(self):
        pass
    
    def __repr__(self):
        return f'Noop()'

    def ejecutar(self):
        return