class CompilationError(Exception):
    pass

class InvalidInclude(Exception):
    pass

class IPIntegrityViolation(Exception):
    print(f'Se rompió la integridad del programa y el IP.\nSe corta ejecución de programa.')
    pass
    #exit()