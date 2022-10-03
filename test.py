from Models.gramatica import Gramatica

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