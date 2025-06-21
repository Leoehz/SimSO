from core.models.Registro import Registro as R
import time

class PreservadorIP:
    def __init__(self):
        self.IP_preservada = None

    def setValorIP(self, valor):
        if (self.IP_preservada == None):
            fset = [valor]
            print(fset)
            #time.sleep(10)
            self.IP_preservada = frozenset(fset)
    # Mientras haya instrucciones segui ejecutando    

    def getValorIP(self):
        return list(self.IP_preservada)[0]
        