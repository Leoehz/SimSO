import re
from core.models.instructions import (Mov, 
                                      Add, 
                                      Inc, 
                                      Dec)

instrucciones_validas = [Mov, Add, Inc, Dec]
inst_factory = {inst.SYNTAX: inst for inst in instrucciones_validas}

### Revisa las instrucciones validas seguidas de espacios y luego los parametros
inst_pattern = f"^({'|'.join([inst.SYNTAX for inst in instrucciones_validas])})" + r'\s+([\w,\s]+)'

def valid_line(line: str) -> re.Match:
    match = re.search(inst_pattern, line)
    return match

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

