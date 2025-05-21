
class Ejecutable:
    def __init__(self,instrucciones: list[str], codigo_fuente: list[str], lookup_table: dict[str, int], entry_point: int, executable_name: str):
        self.entry_point = entry_point
        self.instrucciones = instrucciones
        self.codigo = codigo_fuente
        self.lookup_table = lookup_table
        self.name = executable_name

    def getEntryPoint(self):
        return self.entry_point

    def getLookupTable(self):
        return self.lookup_table

    def getInstrucciones(self):
        return self.instrucciones

    def getInstruccion(self, IP):
        return self.instrucciones[IP]
    
    def getCodigo(self):
        return self.codigo
    
    def getName(self):
        return self.name
