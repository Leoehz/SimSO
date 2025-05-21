import os
from config import LIBS_FOLDER
from utils.validators import valid_line, validate_instruct, validate_params, TypeLine, ENTRYPOINT_LABEL
from core.models.instructions import Noop
from core.models.Ejecutable import Ejecutable
from exceptions import CompilationError, InvalidInclude

class Ensamblador:

	def __init__(self):
		pass

	def compilar(self, path: str, include_list: list = []) -> Ejecutable:
		instrucciones = []
		codigo_fuente = []
		lookup_table = {}
		entry_point = -1
		error_flag = False
		errores = []

		with open(path, 'r') as file_to_read:
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

						instrucciones.append(inst(label=label))
						codigo_fuente.append(line)
						label_line = len(instrucciones)-1
						lookup_table[label] = label_line

						if label == ENTRYPOINT_LABEL:
							entry_point = label_line

					elif type_line == TypeLine.include:
						include_file = str(match.group(1))
						include_path = os.path.join(os.getcwd(), LIBS_FOLDER, include_file)

						if not os.path.exists(include_path):
							raise InvalidInclude(f'El archivo {include_file} no existe en la carpeta de librerias. Ruta de librerias: {LIBS_FOLDER}.')

						if include_file in include_list:
							raise InvalidInclude(f'Referencia circular al intentar importar {include_file} al ensamblar {path}.')
						
						include_list.append(include_file)
						include_exec = self.compilar(path=include_path, include_list=include_list)

						new_main_label = f'main_{include_file.replace('.asm', '')}'
						new_main_noop = Noop(label=new_main_label)

						include_instrucciones = [	new_main_noop if type(x) == Noop and str(x) == 'main:' else x 
							   						for x in include_exec.getInstrucciones()]
						include_codigo = [	f'{new_main_label}:' if x == 'main:' else x 
							   				for x in include_exec.getCodigo()]

						inst = validate_instruct(inst='noop')
						instrucciones.append(inst(label=f'Include("{include_file}")'))
						instrucciones.extend(include_instrucciones)
						instrucciones.append(inst(label=f'EndInclude("{include_file}")'))

						codigo_fuente.append(line)
						codigo_fuente.extend(include_codigo)
						codigo_fuente.append('Fin de Include')

					else:
						raise SyntaxError('Sintaxis no valida.')
				except Exception as e:
					error_txt = f'Error: {e}. Linea: {len(instrucciones)-1} - "{line}". '
					errores.append(error_txt)
					error_flag = True
					continue

		if entry_point == -1:
			raise CompilationError(f'El codigo no contiene la etiqueta de inicio de codigo "{ENTRYPOINT_LABEL}"')

		if error_flag:
			raise CompilationError(f'Se detectaron errores en la compilacion. Abortando operacion.\nDetalle: {errores}')

		ejecutable = Ejecutable(instrucciones=instrucciones,
						  		codigo_fuente=codigo_fuente,
								lookup_table=lookup_table,
								entry_point=entry_point,
								executable_name=os.path.basename(path)
								)

		return ejecutable