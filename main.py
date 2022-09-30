from ast import List
from Models.gramatica import Gramatica

class Main:
    """Ejecuta el programa"""

    gramatica: Gramatica
    cadenaNoTerminales: str
    cadenaTerminales: str
    cadenaProducciones: str
    listaNoTerminales: List[str]
    listaTerminales: List[str]
    listaProducciones: List[List[str]]
    # grafica: Grafica

    def __init__(self) -> None:
        self.prepararListas()

    def prepararListaNoTerminales(self) -> None:
        self.listaNoTerminales = self.cadenaNoTerminales.split(",")

    def prepararListaTerminales(self) -> None:
        self.listaTerminales = self.cadenaTerminales.split(",")

    def prepararListaProducciones(self) -> None:
        pass

    def prepararListas(self) -> None:
        self.prepararListaNoTerminales()
        self.prepararListaTerminales()
        self.prepararListaProducciones()

    def generarAnalisis(self, cadenaNoTerminales: str, cadenaTerminales: str, cadenaProducciones) -> None:
        self.cadenaNoTerminales = cadenaNoTerminales
        self.cadenaTerminales = cadenaTerminales
        self.cadenaProducciones = cadenaProducciones

    def generarTabla(self) -> None:
        pass

if __name__ == "__main__":
    Main()