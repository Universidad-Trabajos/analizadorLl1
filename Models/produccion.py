from typing import List


class Produccion:
    noTerminal: str
    derivacion: str

    def __init__(self, noTerminal: str, derivacion: str) -> None:
        self.noTerminal = noTerminal
        self.derivacion = derivacion
        
    def obtenerPrimerSimbolo(self, noTerminales: List[str], terminales: List[str]) -> list:
        # buscar si el primer simbolo es un noTerminal
        for noTerminal in noTerminales:
            if self.derivacion.find(noTerminal) != -1:
                if self.derivacion.index(noTerminal) == 0:
                    return noTerminal

        # buscar si el primer simbolo es un terminal
        for terminal in terminales:
            if self.derivacion.find(terminal) != -1:
                if self.derivacion.index(terminal) == 0:
                    return terminal

    def obtenerDerivacion(self) -> str:
        pass

    def __str__(self) -> str:
        return ("{} -> {}".format(self.noTerminal, self.derivacion))