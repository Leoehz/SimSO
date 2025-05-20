import re
from enum import Enum
from typing import Tuple
from core.models.instructions import (Mov, 
                                      Add, 
                                      Inc, 
                                      Dec,
                                      Jmp,
                                      Jnz,
                                      Cmp,
                                      Noop)

instrucciones_validas = [Mov, Add, Inc, Dec, Jmp, Jnz, Cmp, Noop]
inst_factory = {inst.SYNTAX: inst for inst in instrucciones_validas}
ENTRYPOINT_LABEL = 'main'

### Revisa las instrucciones validas seguidas de espacios y luego los parametros
inst_pattern = f"^({'|'.join([inst.SYNTAX for inst in instrucciones_validas])})" + r"\s*([\w,\s]*)"
# Identifica una etiqueta
label_pattern = r"(\w+):"

class TypeLine(Enum):
    NULL = 0
    inst = 1
    label = 2

def valid_line(line: str) -> Tuple[re.Match, TypeLine]:
    match = re.search(inst_pattern, line)
    if match:
        return (match, TypeLine.inst)

    match = re.search(label_pattern, line)
    if match:
        return (match, TypeLine.label)
    return (match, TypeLine.NULL)

def validate_instruct(inst: str) -> object:
    return inst_factory[inst]

def validate_params(inst: object, params: list) -> list:
    valid_params = inst.PARAMS_TYPE
    result = []

    for param, valid_types in zip(params, valid_params):
        casted = False
        param = param.strip()
        for valid_type in valid_types:
            try:
                casted_param = valid_type(param)
                casted = True
                result.append(casted_param)
                break
            except Exception:
                continue
        if not casted:
            raise ValueError(f'Error al castear el parametro "{param}"')
        
    return result