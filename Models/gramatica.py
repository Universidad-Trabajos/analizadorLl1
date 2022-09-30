from typing import List
from Models.primeros import Primeros
from Models.produccion import Produccion

class Gramatica:
    """Conjunto de producciones de la gramatica"""

    noTerminales: List[str]
    terminales: List[str]
    producciones: List[Produccion]
    primeros: List[Primeros]

    def __init__(self, noTerminales: List[str], terminales: List[str], producciones: List[Produccion]) -> None:
        self.noTerminales = noTerminales
        self.terminales = terminales
        self.producciones = producciones

    def obtenerPrimero(self, noTerminal: str) -> List[str]:
        pass

    def cargarPrimeros(self) -> None:
        pass