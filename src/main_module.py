from core.models.instructions import Mov
from core.models.Ensamblador import Ensamblador

Mov(1, 2)
ens = Ensamblador(path=r'.\asm\mov.asm')
instrucciones, lookup_table, error = ens.parsear()

for c in ens.codigo_fuente:
    print(c)

print(ens.instrucciones)
print(lookup_table)
print(error)