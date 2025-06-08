from core.models.instructions import Mov
from core.models.Ensamblador import Ensamblador
from core.models.Procesador import Procesador
from core.models.Registro import Registro as R
from core.models.Proceso import Proceso
from core.models.SistemaOperativo import SistemaOperativo
import sys

#Mov(1, 2)
#ens = Ensamblador(path=r'.\asm\mov2.asm')
#ens = Ensamblador(path=r'.\asm\add.asm')
#ens = Ensamblador(path=r'.\asm\add_inc_cmp.asm')
#ens = Ensamblador(path=r'.\asm\test_stack.asm')

def main(argv, arc):
	ens = Ensamblador()
	ejecutables = []
	print(argv)
	for arg in argv:
		ejecutable = ens.compilar(path=arg.replace('\\', '/'))
		print(ejecutable.getInstrucciones())
		#ejecutable = ens.compilar(path=r'.\asm\include.asm')
		ejecutables.append(ejecutable)
		

	procesador = Procesador()
	sistema = SistemaOperativo(ejecutables, procesador)
	procesador.setSistemaOperativo(sistema)
	procesador.procesar()

if __name__ == '__main__':
    main(sys.argv[1:], len(sys.argv[1:]))