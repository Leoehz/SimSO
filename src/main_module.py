from core.models.instructions import Mov, Add
from core.models.Ensamblador import Ensamblador
from core.models.Ejecutable import Ejecutable

Mov(1, 2)
ens = Ensamblador(path=r'.\asm\mov.asm')

print(ens.parsear())

ejecutable = ens.compilar()

#ejecutable.ejectar()