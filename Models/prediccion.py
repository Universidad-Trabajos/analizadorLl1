from copy import copy
from typing import List
from Models.produccion import Produccion


class Prediccion:

    produccion: Produccion
    conjuntoPrediccion: List[str] = []

    def __init__(self, produccion: Produccion, noTerminales: List[str], terminales: List[str], cb_simboloEs, cb_siguientesExistentes, cb_primerosExistentes) -> None:
        self.produccion = produccion
        self.__encontrarConjuntoPrediccion(noTerminales, terminales, cb_simboloEs, cb_siguientesExistentes, cb_primerosExistentes)

    def __encontrarConjuntoPrediccion(self, noTerminales: List[str], terminales: List[str], cb_simboloEs, cb_siguientesExistentes, cb_primerosExistentes) -> None:
        """
        Encuentra el conjunto prediccion correspondiente a la produccion.
        """

        # Obtener el primer simbolo de la derivacion
        primerSimbolo = self.produccion.obtenerPrimerSimbolo(noTerminales, terminales)

        # Obtener el tipo de simbolo
        tipoSimbolo = cb_simboloEs(primerSimbolo)

        '''
        Si el simbolo es "terminal" agregarlo al conjunto prediccion, si
        es "noTerminal" agregar los primeros simbolos de la no terminal de
        la produccion.
        '''
        self.conjuntoPrediccion = []
        if tipoSimbolo == "terminal":
            self.conjuntoPrediccion.append(primerSimbolo)
        elif tipoSimbolo == "noTerminal":
            self.conjuntoPrediccion = cb_primerosExistentes(primerSimbolo)

        '''
        Si entre los elementos del conjunto prediccion está lambda
        agregar los siguientes de la no terminal de la produccion
        '''
        if "λ" in self.conjuntoPrediccion:
            self.conjuntoPrediccion = cb_siguientesExistentes(
                self.produccion.noTerminal)

    def __cadenaElementos(self) -> str:
        cadena: str = ""
        count = 0
        for noTerminal in self.conjuntoPrediccion:
            if count == len(self.conjuntoPrediccion) - 1:
                cadena = cadena + str(noTerminal)
            else:
                cadena = cadena + str(noTerminal) + ", "
            count += 1
        return '{' + cadena+'}'

    def __str__(self) -> str:
        texto = "cp({}) = {}"
        return texto.format(self.produccion, self.__cadenaElementos())