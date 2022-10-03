from typing import List


class Primeros:
    noTerminal: str
    conjuntoNoTerminales: List[str]

    def __init__(self, noTerminal:str, conjuntoNoTerminales:List[str]) -> None:
        self.noTerminal = noTerminal
        self.conjuntoNoTerminales = conjuntoNoTerminales

    def cadenaNoTerminales(self) -> str:
        cadena = ""
        count = 0
        for noTerminal in self.conjuntoNoTerminales:
            if count == len(self.conjuntoNoTerminales):
                cadena += noTerminal
            else:
                cadena += noTerminal + ", "
        return cadena

    def __str__(self) -> str:
        texto = "prim({}) = {{}}"
        return texto.format(self.noTerminal, self.cadenaNoTerminales)
