from enum import StrEnum

class Estado(StrEnum):
    ACTIVO = 'Activo'
    BLOQUEADO = 'Bloqueado'
    FINALIZADO = 'Finalizado'
    EJECUTANDO = 'Ejecutando'
    INACTIVO = 'Inactivo'