from tkinter.ttk import Separator
from typing import List
from Models.gramatica import Gramatica
from View.grafica import Grafica


class Main:
    """Ejecuta el programa"""

    gramatica: Gramatica
    cadenaNoTerminales: str
    cadenaTerminales: str
    cadenaProducciones: str
    listaNoTerminales: List[str] = []
    listaTerminales: List[str] = []
    listaProducciones: List[List[str]]
    grafica: Grafica

    def __init__(self) -> None:
        # self.prepararListas()
        # self.gramatica = Gramatica(self.listaNoTerminales, self.listaTerminales, self.listaProducciones)
        # self.gramatica.cargarPrimeros()
        grafica = Grafica(self.generarAnalisis)
        gramatica = Gramatica(self.listaNoTerminales,
                              self.listaTerminales, self.listaProducciones)

    def prepararListaNoTerminales(self) -> None:
        listaNoTerminal = self.cadenaNoTerminales.split(",")
        for noTerminal in listaNoTerminal:
            self.listaNoTerminales.append(noTerminal.strip())

    def prepararListaTerminales(self) -> None:
        listaTerminal = self.cadenaTerminales.split(",")
        for terminal in listaTerminal:
            self.listaTerminales.append(terminal.strip())

    def prepararListaProducciones(self) -> None:
        # Definir listas para las producciones
        separador = '\n'
        listaProducciones1 = self.cadenaProducciones.split(separador)
        self.listaProducciones = self.retornarProducciones(listaProducciones1)

    def retornarProducciones(self, listaProducciones1):
        produccion = []
        for producciones in listaProducciones1:
            inicio = producciones.split("->")
            if "|" in producciones:
                derivacion = inicio[1].split("|")
                for i in derivacion:
                    produccion.append([inicio[0], i])
            else:
                produccion.append(inicio)
        return produccion

    def prepararListas(self) -> None:
        self.prepararListaNoTerminales()
        self.prepararListaTerminales()
        self.prepararListaProducciones()

        print(self.listaNoTerminales)
        print(self.listaTerminales)

    def generarAnalisis(self, cadenaNoTerminales: str, cadenaTerminales: str, cadenaProducciones: str) -> None:
        self.cadenaNoTerminales = cadenaNoTerminales
        self.cadenaTerminales = cadenaTerminales
        self.cadenaProducciones = cadenaProducciones

        self.prepararListas()

        # print("No terminales: ", self.cadenaNoTerminales)
        # print("Terminales: ", self.cadenaTerminales)
        # print("Producciones: ", self.cadenaProducciones)

    def generarTabla(self) -> None:
        pass


if __name__ == "__main__":
    Main()
