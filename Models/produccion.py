from copy import copy
from typing import List


class Produccion:
    noTerminal: str
    derivacion: str

    def __init__(self, noTerminal: str, derivacion: str) -> None:
        self.noTerminal = noTerminal
        self.derivacion = derivacion
        
    def obtenerPrimerSimbolo(self, noTerminales: List[str], terminales: List[str]) -> str:
        """
        Se posiciona al principio de la derivacion y obtiene el primer simbolo, ya sea terminal o noTerminal.
        """

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

    def contieneNoTerminal(self, noTerminal: str, noTerminales: List[str]) -> bool:
        """
        Retorna True si la produccion contiene el noTerminal dado.
        """
        copiaDerivacion = copy(self.derivacion)

        # Si la noTerminal no tiene comilla simple las noTerminales que
        # tienen comilla simple se deben de quitar de la derivacion
        if noTerminal.find("'") == -1:
            for noTerminalItem in noTerminales:
                if noTerminalItem.find("'") != -1:
                    copiaDerivacion = copiaDerivacion.replace(noTerminalItem, "")

        return copiaDerivacion.find(noTerminal) != -1

    def obtenerSimboloSiguiente(self, noTerminal: str, noTerminales: List[str], terminales: List[str]) -> str:
        """
        Retorna el simbolo siguiente al noTerminal dado, ya sea terminal o noTerminal.
        """

        # # buscar el indice del noTerminal
        # indice = self.derivacion.index(noTerminal)

        # # obtener los caracteres que estan despues del noTerminal
        # caracteresSiguientes = self.derivacion[indice + 1:]

        caracteresSiguientes = self.derivacion.split(noTerminal)[1]

        # si no existe caracteres siguientes, retornar lambda
        if caracteresSiguientes == "":
            return "λ"

        # obtener el primer simbolo de los caracteres siguientes
        # buscar si el primer simbolo es un noTerminal
        for noTerminal in noTerminales:
            if caracteresSiguientes.find(noTerminal) != -1:
                if caracteresSiguientes.index(noTerminal) == 0:
                    return noTerminal

        # buscar si el primer simbolo es un terminal
        for terminal in terminales:
            if caracteresSiguientes.find(terminal) != -1:
                if caracteresSiguientes.index(terminal) == 0:
                    return terminal

    def __str__(self) -> str:
        return ("{} -> {}".format(self.noTerminal, self.derivacion))