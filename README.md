# SimSO - Simulador Simple de SO/CPU

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) SimSO es un simulador de un sistema operativo o procesador simple, desarrollado en Python. Está diseñado para interpretar y ejecutar un conjunto definido de instrucciones en lenguaje ensamblador, permitiendo estudiar los conceptos básicos de la ejecución de programas a bajo nivel.

## Características Principales

* **Interpretación de Ensamblador**: Parsea archivos `.asm` que contienen un conjunto específico de instrucciones.
* **Simulación de Ejecución**: Ejecuta paso a paso (o de forma continua) las instrucciones cargadas.
* **Arquitectura Modular**: Código organizado en núcleo, modelos, interfaces y utilidades para facilitar la extensión.
* **Gestión de Instrucciones**: Sistema para definir y catalogar las instrucciones soportadas (ej: `MOV`).
* **Pruebas Unitarias**: Incluye un conjunto de pruebas para verificar la funcionalidad de los componentes clave.

## Estructura del Proyecto
```
📂 SimSO/
│   app.py              # Punto de entrada principal para ejecutar la simulación
│   LICENSE             # Información detallada de la licencia del proyecto
│   README.md           # Este archivo de documentación
│   .gitignore          # Especifica archivos y directorios ignorados por Git
│   requirements.txt    # Lista de dependencias Python
│
├─── 📂src                 # Directorio principal del código fuente del simulador
│    │   __init__.py
│    │   config.py         # Módulo para manejar configuraciones (si aplica)
│    │   exceptions.py     # Definición de excepciones personalizadas del simulador
│    │   main_module.py    # (A describir) Módulo principal de orquestación o lógica
│    │
│    ├─── 📂asm             # Contiene ejemplos de código en lenguaje ensamblador
│    │       mov.asm       # Ejemplo utilizando la instrucción MOV
│    │
│    ├─── 📂core            # Núcleo lógico del simulador
│    │   │   __init__.py
│    │   └─── 📂models      # Clases que representan los componentes principales
│    │        │   __init__.py
│    │        │   Ejecutable.py  # Representa un programa cargado o en ejecución
│    │        │   Ensamblador.py # Responsable de parsear el código .asm
│    │        └───instructions # Implementación concreta de cada instrucción ASM
│    │           │   __init__.py
│    │           │   catalog.py     # Gestiona/registra las instrucciones disponibles
│    │           │   Mov.py         # Implementación específica de la instrucción MOV
│    │
│    ├─── 📂interfaces    # Define interfaces o clases base abstractas
│    │    │   __init__.py
│    │    │   Instruccion.py # Interfaz/ABC para todas las instrucciones
│    │
│    └─── 📂utils         # Módulos con utilidades generales reutilizables
│         │   __init__.py
│         │   helpers.py      # Funciones de ayuda diversas
│         │   validators.py   # Funciones o clases para validación de datos/entradas
│
└─── 📂tests               # Contiene las pruebas automatizadas del proyecto
│    __init__.py       # Marca 'tests' como un paquete
├─── 📂test_models   # Pruebas para los componentes en src/core/models
│       ...
└─── 📂test_utils    # Pruebas para las utilidades en src/utils
```