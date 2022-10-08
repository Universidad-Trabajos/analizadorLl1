from typing import List
from Models.gramatica import Gramatica
from Models.Helpers.helperListas import agregarElementoSinRepetir
from Models.produccion import Produccion

## AGREGAR ELEMENTOS SIN REPETIR A LISTA
# lista = ["a", "b", "c"]
# lista = agregarElementoSinRepetir(lista, ["d"])
# print(lista)

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
# conjunto = set()
# conjunto.add("a")
# simbolo = "ba"
# conjunto.update(simbolo)
# print(conjunto)

## QUITAR ESPACIOS PRINCIPIO Y FINAL CADENA
# cadena = " EA "
# cadena = cadena.strip()
# print("B"+cadena+"A")

## OBTENER EL SIGUIENTE SIMBOLO DADO UN NO TERMINAL
# noTerminales = ["A", "B", "C"]
# terminales = ["a", "b", "m", "f", "gh", "c", "λ"]
# produccion = Produccion("A", "aB")
# simboloSiguiente = produccion.obtenerSimboloSiguiente("B", noTerminales, terminales)
# print(simboloSiguiente)

## REMOVER UN ELEMENTO DE UNA LISTA
# lista = ["a", "b", "λ"]
# lista.remove("λ")
# print(lista)

## OBTENER LOS SIGUIENTES DE TODOS LOS NO TERMINALES
noTerminales = ["E", "E'", "T", "T'", "F"]
terminales = ["+", "*", "(", ")", "id"]
producciones = [
    ["E", "TE'"],
    ["E'", "+TE'"],
    ["E'", "λ"],
    ["T", "FT'"],
    ["T'", "*FT'"],
    ["T'", "λ"],
    ["F", "(E)"],
    ["F", "id"]
]
gramatica = Gramatica(noTerminales, terminales, producciones)
for prediccion in gramatica.predicciones:
    print(prediccion)
# for primero in gramatica.primeros:
#     print(primero)
# print()
# for siguiente in gramatica.siguientes:
#     print(siguiente)

## LA PRODUCCION CONTIENE UN NO TERMINAL
# noTerminales = ["E", "E'", "T", "T'", "F"]
# produccion = Produccion("E", "TE'")
# print(produccion.contieneNoTerminal("E", noTerminales))

## CONOCER SIMBOLO SIGUIENTE
# noTerminales = ["E", "E'", "T", "T'", "F"]
# terminales = ["+", "*", "(", ")", "id"]
# produccion = Produccion("E", "TE'")
# simboloSiguiente = produccion.obtenerSimboloSiguiente("T", noTerminales, terminales)
# print("Simbolo siguiente: ", simboloSiguiente)

## ENCONTRAR SIMBOLO DESPUÉS DE UN SIMBOLO DADO
# cadena = "TE'"
# simbolosDespuesDe = "E'"
# tajadas = cadena.split(simbolosDespuesDe)
# print(tajadas)

## SABER SI UN SIMBOLO ESTÁ EN UNA CADENA
# cadena = "A'BE'C'a"
# simbolo = "A'"
# indiceLugarSimbolo = cadena.find(simbolo)
# if indiceLugarSimbolo != -1:
#     print("Si está", indiceLugarSimbolo)

## ORDENAR LISTA NO TERMINALES, LOS DE COMILLAS SIMPLES AL PRINCIPIO
# noTerminales = ["E", "E'", "T", "T'", "F"]
# noTerminalesOrdenados = []
# # Los no terminales con comillas simples al principio
# for noTerminal in noTerminales:
#     if noTerminal.find("'") != -1:
#         noTerminalesOrdenados.append(noTerminal)
# # Quitar los no terminales con comillas simples de la lista original
# for noTerminal in noTerminalesOrdenados:
#     noTerminales.remove(noTerminal)
# # Agregar los no terminales sin comillas simples al final
# for noTerminal in noTerminales:
#     noTerminalesOrdenados.append(noTerminal)
# print(noTerminalesOrdenados)

## ORDENAR LISTA NO TERMINALES, LOS DE COMILLAS SIMPLES AL PRINCIPIO
# noTerminales = ["E", "E'", "T", "T'", "F"]
# noTerminales.sort(key=lambda x: x.find("'"), reverse=True)
# print(noTerminales)

## SABER SI UN ELEMENTO ESTÁ EN UNA LISTA
# lista = ["a", "b", "c"]
# elemento = 'a'
# if elemento in lista:
#     print("Si está")

## OBTENER PRIMER SIMBOLO DE LA DERIVACION
# noTerminales = ["E", "E'", "T", "T'", "F"]
# terminales = ["+", "*", "(", ")", "id"]
# produccion = Produccion("E", "E'")
# primerSimbolo = produccion.obtenerPrimerSimbolo(noTerminales, terminales)
# print("Primer simbolo: ", primerSimbolo)