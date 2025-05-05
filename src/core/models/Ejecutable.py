class Ejecutable:
    def __init__(self):
        self.entry_point = []
        self.instrucciones = []
        self.lookup_table = []
        self.errores = []

    def insertarInstrucciones(self, instrucciones, errores):
        self.instrucciones = instrucciones
        self.errores = errores
        #if self.error[0]:
        #    print(self.error[1])
        #    raise Exception

    def definirEntryPoint(self, entry_point):
        self.entry_point = entry_point

    def crearLookupTable(self, lookup_table):
        self.lookup_table = lookup_table

    def getInstrucciones(self):
        return self.instrucciones

    def getInstruccion(self, IP):
        return self.instrucciones[IP]

    def ejecutar(self, IP):
        self.instrucciones[IP].ejecutar()