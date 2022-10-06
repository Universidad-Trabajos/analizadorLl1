from typing import List


class Siguientes:
    noTerminal: str
    conjuntoNoTerminales: List[str]

    def __init__(self, noTerminal: str, conjuntoNoTerminales: List[str]) -> None:
        self.noTerminal = noTerminal
        self.conjuntoNoTerminales = conjuntoNoTerminales

    def cadenaNoTerminales(self) -> str:
        cadena: str = ""
        count = 0
        for noTerminal in self.conjuntoNoTerminales:
            if count == len(self.conjuntoNoTerminales) - 1:
                cadena = cadena + str(noTerminal)
            else:
                cadena = cadena + str(noTerminal) + ", "
            count += 1
        return '{' + cadena+'}'

    def __str__(self) -> str:
        texto = "sig({}) = {}"
        return texto.format(self.noTerminal, self.cadenaNoTerminales())
