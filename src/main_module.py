from core.models.instructions import Mov, Add
from core.models.Ensamblador import Ensamblador

Mov(1, 2)
ens = Ensamblador(path=r'.\asm\mov.asm')

print(ens.parsear())