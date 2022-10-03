from typing import List, Set
from Models.primeros import Primeros
from Models.produccion import Produccion
from Models.Helpers.helperListas import agregarElementoSinRepetir

class Gramatica:
    """Conjunto de producciones de la gramatica"""
    noTerminales: List[str] = []
    terminales: List[str] = ["λ"]
    producciones: List[Produccion] = []
    primeros: List[Primeros] = []

    def __init__(self, noTerminales: List[str], terminales: List[str], producciones: List[List[str]]) -> None:
        self.noTerminales = noTerminales
        self.terminales += terminales
        self.__cargarProducciones(producciones)

    def __cargarProducciones(self, producciones: List[List[str]]) -> None:
        """
        Carga las producciones de la gramatica.
        ["E", "TE'"]:

        noTerminal: E
        derivacion: TE'
        """
        for produccion in producciones:
            nuevaProduccion = Produccion(produccion[0], produccion[1])
            self.producciones.append(nuevaProduccion)

    def __simboloEs(self, simbolo: str) -> str:
        """
        Dado un simbolo, retorna si es "terminal" o "noTerminal".
        """
        if simbolo in self.noTerminales:
            return "noTerminal"
        elif simbolo in self.terminales:
            return "terminal"
        else:
            return "error"

    def __obtenerProducciones(self, noTerminal: str) -> List[Produccion]:
        """
        Retorna todas las producciones del noTerminal dado.
        """
        # retornar todas las producciones que tengan como noTerminal el parametro
        produccionesCoincidentes = []
        for produccion in self.producciones:
            if produccion.noTerminal == noTerminal:
                produccionesCoincidentes.append(produccion)

        return produccionesCoincidentes

    def __obtenerSimbolosPrimeros(self, noTerminal: str) -> List[str]:
        """
        Obtener los primeros simbolos de un noTerminal. Retorna un conjunto.
        """
        # obtener los primeros simbolos de la noTerminal dada
        producciones = self.__obtenerProducciones(noTerminal)
        simbolosPrimeros = []
        for produccion in producciones:

            simbolo = produccion.obtenerPrimerSimbolo(self.noTerminales, self.terminales)

            # si es "terminal" agregarlo a la lista
            if self.__simboloEs(simbolo) == "terminal":
                agregarElementoSinRepetir(simbolosPrimeros, simbolo)

            # si es "noTerminal" agregar los primeros de ese noTerminal
            elif self.__simboloEs(simbolo) == "noTerminal":
                agregarElementoSinRepetir(simbolosPrimeros, self.__obtenerSimbolosPrimeros(simbolo))
            else:
                print("Error: simbolo no reconocido")
        print(f"Primeros de {noTerminal}: {simbolosPrimeros}")
        return simbolosPrimeros

    def cargarTodosLosPrimeros(self) -> None:
        """
        Encuentra los primeros de todos los noTerminales de la gramatica.
        """
        for noTerminal in self.noTerminales:
            primerosSimbolos = self.__obtenerSimbolosPrimeros(noTerminal)
            # print(f"Primeros de {noTerminal}: {primerosSimbolos}")
            # primeros = Primeros(noTerminal, primerosSimbolos)
            # self.primeros.append(primeros)