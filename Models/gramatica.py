from typing import List, Set
from Models.primeros import Primeros
from Models.produccion import Produccion
from Models.Helpers.helperListas import agregarElementoSinRepetir
from Models.siguientes import Siguientes

class Gramatica:
    """Conjunto de producciones de la gramatica"""
    noTerminales: List[str] = []
    terminales: List[str] = ["λ"]
    producciones: List[Produccion] = []
    primeros: List[Primeros] = []
    siguientes: List[Siguientes] = []

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
                agregarElementoSinRepetir(simbolosPrimeros, [simbolo])

            # si es "noTerminal" agregar los primeros de ese noTerminal
            elif self.__simboloEs(simbolo) == "noTerminal":
                agregarElementoSinRepetir(simbolosPrimeros, self.__obtenerSimbolosPrimeros(simbolo))
            else:
                print("Error: simbolo no reconocido")
        return simbolosPrimeros

    def cargarTodosLosPrimeros(self) -> None:
        """
        Encuentra los primeros de todos los noTerminales de la gramatica.
        """
        for noTerminal in self.noTerminales:
            primerosSimbolos = self.__obtenerSimbolosPrimeros(noTerminal)
            primeros = Primeros(noTerminal, primerosSimbolos)
            self.primeros.append(primeros)

    def __obtenerPrimerosDelNoTerminal(self, noTerminal: str) -> Primeros:
        for primero in self.primeros:
            if primero.noTerminal == noTerminal:
                return primero

    def __obtenerProduccionesQueContengan(self, noTerminal: str) -> List[Produccion]:
        """
        Retorna todas las producciones que contengan al noTerminal dado.
        """
        listaProducciones = []
        for produccion in self.producciones:
            if produccion.contieneNoTerminal(noTerminal):
                listaProducciones.append(produccion)
        return listaProducciones

    def __obtenerSimbolosSiguientes(self, noTerminal: str) -> List[str]:
        simbolosSiguientes = []

        # si es el noTerminal inicial, agregar "$"
        if len(self.siguientes) == 0:
            simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, ["$"])

        # obtener todas las producciones que contengan al noTerminal
        producciones = self.__obtenerProduccionesQueContengan(noTerminal)

        # para cada produccion obtener el simbolo siguiente del noTerminal dado
        for produccion in producciones:
            simboloSiguiente = produccion.obtenerSimboloSiguiente(noTerminal, self.noTerminales, self.terminales)

            # si es "terminal" agregarlo a la lista
            if self.__simboloEs(simboloSiguiente) == "terminal":
                simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, [simboloSiguiente])

            # si es "noTerminal" agregar los primeros de ese noTerminal
            elif self.__simboloEs(simboloSiguiente) == "noTerminal":
                simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, self.__obtenerPrimerosDelNoTerminal(simboloSiguiente))
            
            # si es "λ" agregar los siguientes del noTerminal
            elif simboloSiguiente == "λ":
                # simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, self.__obtenerSimbolosSiguientes(produccion.noTerminal))
                # SE DEBE REVISAR ESTE PASO
                pass
            else:
                print("Error: simbolo no reconocido")

        return simbolosSiguientes

    def cargarTodosLosSiguientes(self) -> None:
        """
        Encuentra los siguientes de todos los noTerminales de la gramática.
        """
        for noTerminal in self.noTerminales:
            siguientesSimbolos = self.__obtenerSimbolosSiguientes(noTerminal)
            siguientes = Siguientes(noTerminal, siguientesSimbolos)
            self.siguientes.append(siguientes)