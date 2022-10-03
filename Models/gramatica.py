from typing import List
from Models.primeros import Primeros
from Models.produccion import Produccion

class Gramatica:
    """Conjunto de producciones de la gramatica"""
    noTerminales: List[str]
    terminales: List[str]
    producciones: List[Produccion]
    primeros: List[Primeros]

    def __init__(self, noTerminales: List[str], terminales: List[str], producciones: List[List[str]]) -> None:
        self.noTerminales = noTerminales
        self.terminales = terminales
        self.producciones = producciones
        self.cargarProducciones()

    def cargarProducciones(self) -> None:
        """
        Carga las producciones de la gramatica.
        ["E", "TE'"]:

        noTerminal: E
        derivacion: TE'
        """
        for produccion in self.producciones:
            nuevaProduccion = Produccion(produccion[0], produccion[1])
            self.producciones.append(nuevaProduccion)

    def simboloEs(self, simbolo: str) -> str:
        if simbolo in self.noTerminales:
            return "noTerminal"
        elif simbolo in self.terminales:
            return "terminal"
        else:
            return "error"

    def obtenerProduccion(self, noTerminal: str) -> Produccion:
        for produccion in self.producciones:
            if produccion.noTerminal == noTerminal:
                return produccion

    def obtenerSimbolosPrimeros(self, noTerminal: str) -> List[str]:
        produccion = self.obtenerProduccion(noTerminal)
        primerSimbolo = produccion.obtenerPrimerSimbolo()

    def obtenerPrimeros(self, noTerminal: str) -> List[str]:
        simbolosPrimeros = []

    def cargarTodosLosPrimeros(self) -> None:
        pass