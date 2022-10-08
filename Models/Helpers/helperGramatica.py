from typing import List

from Models.prediccion import Prediccion


def obtenerTablaConstruida(noTerminales: List[str], terminales: List[str], conjuntosPrediccion: List[Prediccion]) -> List[List[str]]:
        '''
        Retorna una lista de listas, cada lista interna representa una fila de la tabla.
        La tabla retornada contiene todos los datos necesitados: no terminales, terminales
        y producciones.

        Ejemplo:
        [
            ["VT/VN",   "+",        "*",    "id",       "(",        ")",        "$"     ],
            ["E",       "",         "",     "E->TE'",   "E->TE'",   "",         ""      ],
            ["E'",      "E'->TE'",  "",     "",         "",         "E'->λ",    "E'->λ" ],
            ...
        ]

        '''
        
        # Agregar el simbolo $ a la lista de terminales
        terminales.append("$")
        
        tabla = []

        # Definir la primera fila: VT/VN y los terminales
        primeraFila = ["VT/VN"]
        for terminal in terminales:
            primeraFila.append(terminal)
        tabla.append(primeraFila)

        # Por cada no terminal, agregar una fila a la tabla
        for noTerminal in noTerminales:

            # Llenar la fila con el no terminal al principio y cadenas vacías en el resto
            fila = [noTerminal]
            for _ in range(1, len(primeraFila)):
                fila.append("")

            # Obtener los conjuntos prediccion para el no terminal actual
            conjuntosPrediccionNoTerminal = __obtenerConjuntosPrediccionNoTerminal(noTerminal, conjuntosPrediccion)

            # Por cada conjunto prediccion iterar sobre sus terminales
            for conjuntoPrediccion in conjuntosPrediccionNoTerminal:

                terminalesConjuntoPrediccion = conjuntoPrediccion.conjuntoPrediccion

                # Por cada terminal en el conjunto prediccion, buscar dicho terminal en la
                # primera fila, obtener su índice, y agregar la producción en la fila
                # actual usando dicho índice
                for terminal in terminalesConjuntoPrediccion:
                    
                    # Buscar el índice del terminal en la primera fila
                    indiceTerminal = primeraFila.index(terminal)

                    # Agregar la producción en la fila actual usando el índice del terminal
                    fila[indiceTerminal] = conjuntoPrediccion.produccion.__str__()

            # Agregar la nueva fila a la tabla
            tabla.append(fila)

        return tabla

def __obtenerConjuntosPrediccionNoTerminal(noTerminal: str, conjuntosPrediccion: List[Prediccion]) -> List[Prediccion]:
    '''
    Retorna los conjuntos prediccion para un no terminal dado
    '''
    conjuntosPrediccionNoTerminal = []
    for conjuntoPrediccion in conjuntosPrediccion:
        if conjuntoPrediccion.produccion.noTerminal == noTerminal:
            conjuntosPrediccionNoTerminal.append(conjuntoPrediccion)
    return conjuntosPrediccionNoTerminal