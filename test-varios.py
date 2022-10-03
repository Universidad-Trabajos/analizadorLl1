from typing import List
from Models.gramatica import Gramatica

## PRUEBA CON LA GRAMATICA COMPLETA
# noTerminales = ["E", "E'", "T", "T'", "F"]
# terminales = ["+", "*", "(", ")", "id"]
# producciones = [
#     ["E", "TE'"],
#     ["E'", "+TE'"],
#     ["E'", "λ"],
#     ["T", "FT'"],
#     ["T'", "*FT'"],
#     ["T'", "λ"],
#     ["F", "(E)"],
#     ["F", "id"]
# ]
# gramatica = Gramatica(noTerminales, terminales, producciones)
# gramatica.producciones[0].derivacion
# gramatica.cargarTodosLosPrimeros()
# for primeros in gramatica.primeros:
#     print(primeros)

## PRUEBA CON UNA GRAMATICA REDUCIDA
# noTerminales = ["A", "B", "C"]
# terminales = ["a", "b", "m", "f", "gh"]
# producciones = [
#     ["A", "a"],
#     ["A", "b"],
#     ["B", "ghf"],
#     ["B", "Cm"],
#     ["C", "f"]
# ]
# gramatica = Gramatica(noTerminales, terminales, producciones)
# gramatica.cargarTodosLosPrimeros()
# for primeros in gramatica.primeros:
#     print(primeros)

## AGREGAR UNA PRODUCCION A UNA LISTA
# nuevaProduccion = Produccion("E", "TE'")
# listaProducciones: List[Produccion] = []
# listaProducciones.append(nuevaProduccion)

## PRUEBA CON CONJUNTOS
# conjunto1 = {"a", "b", "c"}
# simbolo = "d"
# conjunto1.update(simbolo)
# print(conjunto1)

## PRUEBA CON OBTENER EL INDICE DE UN CARACTER
# cadena = "hola"
# if cadena.find("h") != -1:
#     print(cadena.index("h"))

## PRUEBA CONJUNTO VACIO
# conjunto = set()
# simbolo = "a"
# conjunto.update(simbolo)
# print(conjunto)

## CONVERTIR UN CONJUNTO A UNA LISTA
# conjunto = {"a", "b", "c"}
# lista = list(conjunto)
# print(lista)

## CONJUNTO CON CARACTERES DOBLES
# FIX: No funciona esto: {"a"} union {"ab"}. Problema: divide al segundo conjunto
conjunto = set()
conjunto.add("a")
simbolo = "ba"
conjunto.update(simbolo)
print(conjunto)