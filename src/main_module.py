from core.models.instructions import Mov, Add
from core.models.Ensamblador import Ensamblador
from core.models.Ejecutable import Ejecutable
from core.models.Procesador import Procesador
from core.models.Registro import Registro as R

Mov(1, 2)
ens = Ensamblador(path=r'.\asm\add.asm')

print(ens.parsear())

ejecutable = ens.compilar()
procesador = Procesador(IP=0)

procesador.ejecutar(ejecutable=ejecutable)
print(procesador.getRegister(R.AX))

#ejecutable.ejecutar(IP=0)
#print(ejecutable.)