from utils.validators import valid_line, validate_instruct, validate_params

class Ensamblador:

	def __init__(self, path):
		self.path = path

	def parsear(self):
		instrucciones = []
		codigo_fuente = []
		error_flag = False
		errores = []

		with open(self.path, 'r') as file_to_read:
			for line in file_to_read:
				line = line.strip()
				# Saltear si la linea esta vacia o es un comentario
				if line == '' or line[0] == '#':
					continue

				match = valid_line(line)
				try:
					if match:
						inst = str(match.group(1))
						inst = validate_instruct(inst=inst) # Se obtiene la clase de la instruccion
						params = str(match.group(2))
						params_list = params.split(sep=',')
						params_list = validate_params(inst=inst, params=params_list)
						
						instrucciones.append(inst(*params_list))
						codigo_fuente.append(line)
					else:
						raise SyntaxError(f'Sintaxis no valida.')
				except Exception as e:
					error_txt = f'Error: {e}. Linea: {len(instrucciones)-1} - "{line}". '
					errores.append(error_txt)
					error_flag = True
					continue
				

		error = (error_flag, errores)
		return instrucciones, error