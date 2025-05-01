from utils.validators import valid_line, validate_instruct, validate_params, TypeLine, ENTRYPOINT_LABEL
from ..models.Ejecutable import Ejecutable

class Ensamblador:

	def __init__(self, path):
		self.path = path
		self.instrucciones = []
		self.codigo_fuente = []
		self.lookup_table = {}
		self.entry_point = -1
		self.error_flag = False
		self.errores = []

	def parsear(self):
		instrucciones = []
		codigo_fuente = []
		lookup_table = {}
		entry_point = -1
		error_flag = False
		errores = []

		with open(self.path, 'r') as file_to_read:
			for line in file_to_read:
				line = line.strip()
				# Saltear si la linea esta vacia o es un comentario
				if line == '' or line[0] == '#':
					continue

				match, type_line = valid_line(line)
				try:
					if type_line == TypeLine.inst:
						inst = str(match.group(1))
						inst = validate_instruct(inst=inst) # Se obtiene la clase de la instruccion
						params = str(match.group(2))
						params_list = params.split(sep=',')
						params_list = validate_params(inst=inst, params=params_list)
						
						instrucciones.append(inst(*params_list))
						codigo_fuente.append(line)
					elif type_line == TypeLine.label:
						inst = validate_instruct(inst='noop')
						label = str(match.group(1))

						if label in lookup_table.keys():
							raise Exception(f'La etiqueta "{label}" se encuentra repetida en el codigo.')

						instrucciones.append(inst())
						codigo_fuente.append(line)
						label_line = len(instrucciones)-1
						lookup_table[label] = label_line

						if label == ENTRYPOINT_LABEL:
							entry_point = label_line
					else:
						raise SyntaxError('Sintaxis no valida.')
				except Exception as e:
					error_txt = f'Error: {e}. Linea: {len(instrucciones)-1} - "{line}". '
					errores.append(error_txt)
					error_flag = True
					continue

		if entry_point == -1:
			raise Exception(f'El codigo no contiene la etiqueta de inicio de codigo "{ENTRYPOINT_LABEL}"')

		error = (error_flag, errores)
		# Devolver ejecutable
		return instrucciones, lookup_table, error

	def compilar():
		ejecutable = Ejecutable()
		ejecutable.insertarInstrucciones(self.instrucciones, self.error)
		ejecutable.definirEntryPoint(self.entryPoint)
		ejecutable.crearLookupTable(self.lookUpTable)
		return ejecutable