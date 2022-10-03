class Produccion:
    noTerminal: str
    derivacion: str

    def __init__(self, noTerminal: str, derivacion: str) -> None:
        self.noTerminal = noTerminal
        self.derivacion = derivacion
        
    def obtenerPrimerSimbolo(self) -> str:
        pass

    def obtenerDerivacion(self) -> str:
        pass

    def toString(self) -> str:
        pass