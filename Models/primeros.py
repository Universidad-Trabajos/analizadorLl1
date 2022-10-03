from typing import List


class Primeros:
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
        print(cadena)
        return '{' + cadena+'}'

    def __str__(self) -> str:
        texto = "prim({}) = {}"
        return texto.format(self.noTerminal, self.cadenaNoTerminales())
