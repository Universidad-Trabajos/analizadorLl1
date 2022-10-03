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
    listaNoTerminales: List[str]
    listaTerminales: List[str]
    listaProducciones: List[List[str]]
    grafica: Grafica

    def __init__(self) -> None:
        # self.prepararListas()
        # self.gramatica = Gramatica(self.listaNoTerminales, self.listaTerminales, self.listaProducciones)
        # self.gramatica.cargarPrimeros()
        grafica = Grafica(self.generarAnalisis)

    def prepararListaNoTerminales(self) -> None:
        self.listaNoTerminales = self.cadenaNoTerminales.split(",")

    def prepararListaTerminales(self) -> None:
        self.listaTerminales = self.cadenaTerminales.split(",")

    def prepararListaProducciones(self) -> None:
        # Definir listas para las producciones
        separador = '\n'
        listaProducciones1 = self.cadenaProducciones.split(separador)
        produccion = self.retornarProducciones(listaProducciones1)
        print(produccion)

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

    def generarAnalisis(self, cadenaNoTerminales: str, cadenaTerminales: str, cadenaProducciones: str) -> None:
        self.cadenaNoTerminales = cadenaNoTerminales
        self.cadenaTerminales = cadenaTerminales
        self.cadenaProducciones = cadenaProducciones

        self.prepararListaProducciones()

        # print("No terminales: ", self.cadenaNoTerminales)
        # print("Terminales: ", self.cadenaTerminales)
        # print("Producciones: ", self.cadenaProducciones)

    def generarTabla(self) -> None:
        pass


if __name__ == "__main__":
    Main()
