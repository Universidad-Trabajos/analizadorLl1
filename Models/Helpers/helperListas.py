from typing import List


def agregarElementoSinRepetir(lista1: List[str], lista2: List[str]) -> List :
    """
    Trata de agregar los elementos de la lista2 en la lista1. Si hay elementos repetidos
    los omite y no los agrega.
    """
    # Se verifica que no existan elementos de lista2 en lista1
    for elementoLista2 in lista2:

        elementoCoincide = False

        for elementoLista1 in lista1:
            if elementoLista1 == elementoLista2:
                elementoCoincide = True

        if not elementoCoincide:
            lista1.append(elementoLista2)
    
    return lista1