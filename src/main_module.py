from core.models.instructions import Mov, Add
from core.models.Ensamblador import Ensamblador

Mov(1, 2)
ens = Ensamblador(path=r'C:\Users\ezele\OneDrive\Undav\8° Cuatrimestre\Simulacion y Modelizacion\repos\SimSO\src\asm\mov.asm')

print(ens.parsear())