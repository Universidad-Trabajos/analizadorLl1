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

        # Ordenar la lista de noTerminales; los noTerminales que tienen comilla simple
        # deben de ir al principio de la lista
        copiaNoTerminales = copy(noTerminales)
        copiaNoTerminales.sort(key=lambda x: x.find("'"), reverse=True)
        noTerminalesOrdenados = copiaNoTerminales

        # buscar si el primer simbolo es un noTerminal
        for noTerminal in noTerminalesOrdenados:
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

        '''
        Dado un simbolo cualquiera, se toma toda la parte derecha a dicho simbolo.
        Un ejemplos es:
        cadena = "abcdedf"
        simbolo = "d"
        caracteresSiguientes = "edf"
        '''
        caracteresSiguientes = self.derivacion.split(noTerminal)[1]

        # Ordenar la lista de noTerminales; los noTerminales que tienen comilla simple
        # deben de ir al principio de la lista
        copiaNoTerminales = copy(noTerminales)
        copiaNoTerminales.sort(key=lambda x: x.find("'"), reverse=True)
        noTerminalesOrdenados = copiaNoTerminales

        # si no existe caracteres siguientes, retornar lambda
        if caracteresSiguientes == "":
            return "λ"

        # obtener el primer simbolo de los caracteres siguientes
        
        # buscar si el primer simbolo es un noTerminal
        for noTerminal in noTerminalesOrdenados:
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