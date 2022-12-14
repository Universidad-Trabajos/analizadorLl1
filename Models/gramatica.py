from copy import copy
from typing import List, Set
from Models.prediccion import Prediccion
from Models.primeros import Primeros
from Models.produccion import Produccion
from Models.Helpers.helperListas import agregarElementoSinRepetir
from Models.Helpers.helperGramatica import obtenerTablaConstruida
from Models.siguientes import Siguientes

class Gramatica:
    """Conjunto de producciones de la gramatica"""
    noTerminales: List[str] = []
    terminales: List[str] = []
    producciones: List[Produccion] = []
    primeros: List[Primeros] = []
    siguientes: List[Siguientes] = []
    predicciones: List[Prediccion] = []

    lambdaPresenteEnListaTerminalesOriginal = False

    def __init__(self, noTerminales: List[str], terminales: List[str], producciones: List[List[str]]) -> None:
        # Reset de variables
        self.noTerminales = []
        self.terminales = []
        self.producciones = []
        self.primeros = []
        self.siguientes = []
        self.predicciones = []

        # Asignación de variables y ejecución de métodos iniciales
        self.noTerminales = noTerminales
        self.__agregarLambdaATerminales(terminales)
        self.__cargarProducciones(producciones)
        self.__cargarTodosLosPrimeros()
        self.__cargarTodosLosSiguientes()
        self.__cargarTodosLosConjuntosPrediccion()

    def __agregarLambdaATerminales(self, terminales: List[str]) -> None:
        """
        Agrega el simbolo "λ" a la lista de terminales si no está presente.
        """
        if "λ" not in terminales:
            terminales.append("λ")
        else:
            self.lambdaPresenteEnListaTerminalesOriginal = True
        self.terminales = terminales

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
        # Retornar todas las producciones que tengan como noTerminal el parametro
        produccionesCoincidentes = []
        for produccion in self.producciones:
            if produccion.noTerminal == noTerminal:
                produccionesCoincidentes.append(produccion)

        return produccionesCoincidentes

    def __obtenerSimbolosPrimeros(self, noTerminal: str) -> List[str]:
        """
        Obtener los primeros simbolos de un noTerminal dado.
        """
        # Obtener los primeros simbolos de la noTerminal dada
        producciones = self.__obtenerProducciones(noTerminal)
        simbolosPrimeros = []
        for produccion in producciones:

            simbolo = produccion.obtenerPrimerSimbolo(self.noTerminales, self.terminales)

            # Si es "terminal" agregarlo a la lista
            if self.__simboloEs(simbolo) == "terminal":
                simbolosPrimeros = agregarElementoSinRepetir(simbolosPrimeros, [simbolo])

            # Si es "noTerminal" agregar los primeros de ese noTerminal
            elif self.__simboloEs(simbolo) == "noTerminal":
                simbolosPrimeros = agregarElementoSinRepetir(simbolosPrimeros, self.__obtenerSimbolosPrimeros(simbolo))
            else:
                print("Error: simbolo no reconocido")
        return simbolosPrimeros

    def __cargarTodosLosPrimeros(self) -> None:
        """
        Encuentra los primeros de todos los noTerminales de la gramatica.
        """
        for noTerminal in self.noTerminales:
            primerosSimbolos = self.__obtenerSimbolosPrimeros(noTerminal)
            primeros = Primeros(noTerminal, primerosSimbolos)
            self.primeros.append(primeros)

    def __obtenerConjuntoPrimerosYaExistente(self, noTerminal: str) -> List[str]:
        """
        Retorna la lista de primeros del noTerminal dado.
        """
        for primero in self.primeros:
            if primero.noTerminal == noTerminal:
                return primero.conjuntoNoTerminales

    def __obtenerProduccionesQueContengan(self, noTerminal: str) -> List[Produccion]:
        """
        Retorna todas las producciones que contengan al noTerminal dado.
        """
        listaProducciones = []
        for produccion in self.producciones:
            if produccion.contieneNoTerminal(noTerminal, self.noTerminales):
                listaProducciones.append(produccion)
        return listaProducciones

    def __obtenerConjuntosSimbolosSiguientesYaExistente(self, noTerminal: str) -> List[str]:
        """
        Retorna los siguientes de un noTerminal ya existente. No se realiza el analisis,
        el conjunto de simbolos siguientes existe.
        """
        for siguiente in self.siguientes:
            if siguiente.noTerminal == noTerminal:
                return siguiente.conjuntoNoTerminales

    def __obtenerConjuntosSimbolosSiguientes(self, noTerminal: str) -> List[str]:
        """
        Retorna los simbolos siguientes de un noTerminal dado.
        """
        simbolosSiguientes = []

        # Si es el noTerminal inicial, agregar "$"
        if len(self.siguientes) == 0:
            simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, ["$"])

        # Obtener todas las producciones que contengan al noTerminal
        producciones = self.__obtenerProduccionesQueContengan(noTerminal)

        # Para cada produccion obtener el simbolo siguiente del noTerminal dado
        for produccion in producciones:

            simboloSiguiente = produccion.obtenerSimboloSiguiente(noTerminal, self.noTerminales, self.terminales)

            # Si es "λ" agregar los siguientes del noTerminal
            if simboloSiguiente == "λ":
                # Si el noTerminal de la produccion es diferente al noTerminal dado se
                # agrega los siguientes del noTerminal de la produccion, si son la misma
                # noTerminal, no hacer nada
                if produccion.noTerminal != noTerminal:
                    simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, self.__obtenerConjuntosSimbolosSiguientesYaExistente(produccion.noTerminal))

            # Si es "terminal" agregarlo a la lista
            elif self.__simboloEs(simboloSiguiente) == "terminal":
                simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, [simboloSiguiente])

            # Si es "noTerminal" agregar los primeros de ese noTerminal
            elif self.__simboloEs(simboloSiguiente) == "noTerminal":
                simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, self.__obtenerConjuntoPrimerosYaExistente(simboloSiguiente))

                # Si entre los primeros esta "λ", quitar "λ" de la lista y 
                # agregar los siguientes del noTerminal
                if "λ" in simbolosSiguientes:
                    simbolosSiguientes.remove("λ")
                    simbolosSiguientes = agregarElementoSinRepetir(simbolosSiguientes, self.__obtenerConjuntosSimbolosSiguientesYaExistente(produccion.noTerminal))

            else:
                print("Error: simbolo no reconocido")

        return simbolosSiguientes

    def __cargarTodosLosSiguientes(self) -> None:
        """
        Encuentra los siguientes de todos los noTerminales de la gramática.
        """

        # Cargar los siguientes si los primeros ya fueron cargados
        if len(self.primeros) != 0:

            for noTerminal in self.noTerminales:
                siguientesSimbolos = self.__obtenerConjuntosSimbolosSiguientes(noTerminal)
                siguientes = Siguientes(noTerminal, siguientesSimbolos)
                self.siguientes.append(siguientes)

    def __cargarTodosLosConjuntosPrediccion(self) -> None:
        """
        Carga todos los conjuntos de prediccion de la gramatica.
        """
        
        # Por cada produccion obtener su correspondiente conjunto de prediccion y agregarlo
        # a su lista correspondiente
        for produccion in self.producciones:
            conjuntoPrediccion = Prediccion(
                produccion,
                self.noTerminales,
                self.terminales,
                self.__simboloEs,
                self.__obtenerConjuntosSimbolosSiguientesYaExistente,
                self.__obtenerConjuntoPrimerosYaExistente)
            self.predicciones.append(conjuntoPrediccion)

    def obtenerTablaAnalisisSintactico(self) -> List[List[str]]:
        """
        Retorna la tabla construida de análisis sintáctico.	
        """

        # Si lambda no está presente en la lista original de terminales, quitarlo de la lista
        copiaTerminales = copy(self.terminales)
        if not self.lambdaPresenteEnListaTerminalesOriginal:
            copiaTerminales.remove("λ")
        
        terminalesGramatica = copiaTerminales

        tablaConstruida = obtenerTablaConstruida(self.noTerminales, terminalesGramatica, self.predicciones)
        return tablaConstruida