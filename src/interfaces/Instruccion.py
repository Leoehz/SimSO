from abc import ABC, abstractmethod

class Instruccion(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass