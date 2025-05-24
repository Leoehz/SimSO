from interfaces.Instruccion import Instruccion
from ..Registro import Registro
from ..Procesador import Procesador

class Pop(Instruccion):
    N_PARAMS = 1
    SYNTAX = 'pop'
    PARAMS_TYPE = [(Registro, int)]

    def __init__(self, param1):
        self.param1 = param1

    def __repr__(self):
        return f'Pop({self.param1})'

    def ejecutar(self, procesador, ejecutable):
        try:
            dummy = procesador.getProceso().popValorStack()
        except:
            print("La pila está vacía, se devuelve 0.")
            dummy = 0
        procesador.setRegister(self.param1, dummy)
        return
        #return self.param1
    
    def get_params(self):
        return self.n_params