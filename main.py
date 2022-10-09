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
    grafica: Grafica = None

    def __init__(self) -> None:
        self.grafica = Grafica(self.generarAnalisis)

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

    def retornarProducciones(self, listaProducciones1: List[str]):
        produccion = []
        for producciones in listaProducciones1:
            inicio = producciones.split("->")
            if "|" in producciones:
                derivacion = inicio[1].split("|")
                for i in derivacion:
                    produccion.append([inicio[0].strip(), i.strip()])
            else:
                # strip para cada item interno
                inicio = [inicio[0].strip(), inicio[1].strip()]
                produccion.append(inicio)
        return produccion

    def prepararListas(self) -> None:
        self.prepararListaNoTerminales()
        self.prepararListaTerminales()
        self.prepararListaProducciones()

    def generarAnalisis(self, cadenaNoTerminales: str, cadenaTerminales: str, cadenaProducciones: str) -> List:
        self.cadenaNoTerminales = cadenaNoTerminales
        self.cadenaTerminales = cadenaTerminales
        self.cadenaProducciones = cadenaProducciones

        self.prepararListas()
        gramatica = Gramatica(self.listaNoTerminales,
                              self.listaTerminales, self.listaProducciones)
        listaRetorno = [gramatica.primeros, gramatica.siguientes, gramatica.predicciones, gramatica.obtenerTablaAnalisisSintactico()]
        return listaRetorno
        # self.grafica.generarVentanaResultado()
        # for primero in gramatica.primeros:
        #     print(primero)

    def generarTabla(self) -> None:
        pass


if __name__ == "__main__":
    Main()
