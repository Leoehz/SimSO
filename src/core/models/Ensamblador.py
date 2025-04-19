import re

class Ensamblador:
    def __init__(self, path):
        self.path = path

    def parsear(self):
        instrucciones = []
        error = [False, '']
        with open(self.path, 'r') as file_to_read:
            for line in file_to_read:
                match = re.search('^(mov|add|cmp|inc|dec|jmp|jnz)\s+([\w,\s]+)', str)
                if match:
                  inst = match.group(1)
                  params = match.group(2)
                  if inst == "mov" or inst == "add" or inst == "cmp":
                    match = re.search('^(\w+)\s*,\s*(\w+)\s*$', params)
                    param1 = match.group(1)
                    param2 = match.group(2)
                    if inst == "mov":
                      instrucciones.append(Mov(param1, param2))
                    elif inst == "add"
                      instrucciones.append(Add(param1, param2))
                  elif inst == "inc" or inst == "dec" or inst == "jmp" or inst == "jnz":
                    match = re.search('^(\w+)\s*$', params)
                else:
                    error = [True, 'No hay una instrucción válida']

        return instrucciones, error