from core.models.instructions import Mov
from core.models.Ensamblador import Ensamblador
from core.models.Procesador import Procesador
from core.models.Registro import Registro as R

Mov(1, 2)
#ens = Ensamblador(path=r'.\asm\mov2.asm')
#ens = Ensamblador(path=r'.\asm\add.asm')
#ens = Ensamblador(path=r'.\asm\add_inc_cmp.asm')
ens = Ensamblador()

ejecutable = ens.compilar(path=r'.\asm\include.asm')
procesador = Procesador()

procesador.ejecutar(ejecutable=ejecutable)