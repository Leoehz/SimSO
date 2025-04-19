from enum import StrEnum

# Catalogo de instrucciones validas
class Inst(StrEnum):
    MOV = 'mov'
    ADD = 'add'
    INC = 'inc'
    DEC = 'dec'