from enum import StrEnum

class Registro(StrEnum):
    AX = 'ax'
    BX = 'bx'
    CX = 'cx'
    DX = 'dx'
    IP = 'ip'
    FLAG = 'flag'
    CARRY_FLAG = 'carry_flag'