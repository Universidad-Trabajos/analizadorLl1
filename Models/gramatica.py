from typing import List, Set
from Models.primeros import Primeros
from Models.produccion import Produccion

class Gramatica:
    """Conjunto de producciones de la gramatica"""
    noTerminales: List[str] = []
    terminales: List[str] = ["λ"]
    producciones: List[Produccion] = []
    primeros: List[Primeros] = []

    def __init__(self, noTerminales: List[str], terminales: List[str], producciones: List[List[str]]) -> None:
        self.noTerminales = noTerminales
        self.terminales = terminales
        self.cargarProducciones(producciones)

    def cargarProducciones(self, producciones) -> None:
        """
        Carga las producciones de la gramatica.
        ["E", "TE'"]:

        noTerminal: E
        derivacion: TE'
        """
        for produccion in producciones:
            nuevaProduccion = Produccion(produccion[0], produccion[1])
            self.producciones.append(nuevaProduccion)

    def simboloEs(self, simbolo: str) -> str:
        if simbolo in self.noTerminales:
            return "noTerminal"
        elif simbolo in self.terminales:
            return "terminal"
        else:
            return "error"

    def obtenerProducciones(self, noTerminal: str) -> List[Produccion]:
        # retornar todas las producciones que tengan como noTerminal el parametro
        produccionesCoincidentes = []
        for produccion in self.producciones:
            if produccion.noTerminal == noTerminal:
                produccionesCoincidentes.append(produccion)

        return produccionesCoincidentes

    def obtenerSimbolosPrimeros(self, noTerminal: str) -> Set[str]:
        """
        Obtener los primeros simbolos de un noTerminal. Retorna un conjunto.
        """
        # obtener los primeros simbolos de la noTerminal dada
        producciones = self.obtenerProducciones(noTerminal)
        simbolosPrimeros = set()
        for produccion in producciones:
            simbolo = produccion.obtenerPrimerSimbolo(self.noTerminales, self.terminales)
            # si es "terminal" agregarlo a la lista
            if self.simboloEs(simbolo) == "terminal":
                simbolosPrimeros.update(simbolo)
            # si es "noTerminal" agregar los primeros de ese noTerminal
            elif self.simboloEs(simbolo) == "noTerminal":
                simbolosPrimeros.update(self.obtenerSimbolosPrimeros(simbolo))
            else:
                print("Error: simbolo no reconocido")

        return simbolosPrimeros

    def cargarTodosLosPrimeros(self) -> None:
        for noTerminal in self.noTerminales:
            primerosSimbolos = list(self.obtenerSimbolosPrimeros(noTerminal))
            primeros = Primeros(noTerminal, primerosSimbolos)
            self.primeros.append(primeros)