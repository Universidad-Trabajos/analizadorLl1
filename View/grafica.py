from msilib import Table
import tkinter as tk
from tkinter import END, Entry, scrolledtext, ttk
from typing import List

from Models.prediccion import Prediccion


class Grafica:
    anchoVentana = 700
    altoVentana = 980
    noTerminales = ""
    terminales = ""
    producciones = ""

    def __init__(self, callback):
        self.callback = callback
        # Construir ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Analizador LL1")
        self.ventana.geometry("{0}x{1}".format(
            self.anchoVentana, self.altoVentana
        ))
        self.ventana.resizable(width=False, height=False)
        self.crearEntradas()
        self.ventana.mainloop()

    def crearEntradas(self):
        l = tk.Label(self.ventana, text="Ingrese los no terminales: ")
        l.pack()
        self.entry = tk.Entry(self.ventana)
        self.entry.pack()

        l2 = tk.Label(self.ventana, text="Ingrese los terminales: ")
        l2.pack()
        self.entry2 = tk.Entry(self.ventana)
        self.entry2.pack()

        l3 = tk.Label(self.ventana, text="Ingrese las producciones: ")
        l3.pack()
        self.entry3 = tk.Text(self.ventana)
        self.entry3.pack(padx=280)

        button = tk.Button(self.ventana, text="Generar Análisis",
                           bg="light blue", borderwidth=5, command=lambda: self.ejecutar())
        button.pack()

    def ejecutar(self) -> None:
        self.capturarEntradas()

    def capturarEntradas(self):
        self.noTerminales = self.entry.get()
        self.terminales = self.entry2.get()
        self.producciones = self.entry3.get("1.0", 'end-1c')
        listaRetorno = self.callback(
            self.noTerminales, self.terminales, self.producciones)
        textoNoTerminales = ""
        textoTerminales = ""
        textoConjuntoPrediccion = ""
        for i in listaRetorno[0]:
            textoNoTerminales += str(i) + "\n"
        for i in listaRetorno[1]:
            textoTerminales += str(i) + "\n"
        for i in listaRetorno[2]:
            textoConjuntoPrediccion += str(i) + "\n"

        self.generarVentanaResultado(textoNoTerminales, textoTerminales, textoConjuntoPrediccion)

    def generarVentanaResultado(self, conjuntoPrimeros, conjuntoSiguientes, conjuntoPrediccion) -> None:
        '''Genera la ventana con el resultado del análisis LL1'''
        # Valores por defecto
        self.ventanaResultado = tk.Tk()
        self.ventanaResultado.title("Resultado análisis LL1")
        self.ventana.geometry("{0}x{1}".format(
            self.anchoVentana, self.altoVentana
        ))

        tk.Label(self.ventanaResultado,
                 text="Conjunto Primeros",
                 font=("Arial", 15),
                 background='AntiqueWhite1',
                 foreground="black").grid(column=0,
                                          row=0)

        text_area = scrolledtext.ScrolledText(self.ventanaResultado,
                                              wrap=tk.WORD,
                                              width=40,
                                              height=5,
                                              font=("Arial",
                                                    15))

        tk.Label(self.ventanaResultado,
                 text="Conjunto Siguientes",
                 font=("Arial", 15),
                 background='AntiqueWhite1',
                 foreground="black").grid(column=0,
                                          row=2)

        text_area2 = scrolledtext.ScrolledText(self.ventanaResultado,
                                               wrap=tk.WORD,
                                               width=40,
                                               height=5,
                                               font=("Arial",
                                                     15))

        tk.Label(self.ventanaResultado,
                 text="Conjunto Predicción",
                 font=("Arial", 15),
                 background='AntiqueWhite1',
                 foreground="black").grid(column=0,
                                          row=4)

        text_area3 = scrolledtext.ScrolledText(self.ventanaResultado,
                                               wrap=tk.WORD,
                                               width=40,
                                               height=5,
                                               font=("Arial",
                                                     15))

        tk.Label(self.ventanaResultado,
                 text="Tabla Análisis Sintáctico",
                 font=("Arial", 15),
                 background='AntiqueWhite1',
                 foreground="black").grid(column=0,
                                          row=6)

        text_area.grid(column=0, row=1, pady=10, padx=10)
        text_area.insert(tk.INSERT, conjuntoPrimeros)
        text_area.configure(state='disabled')

        text_area2.grid(column=0, row=3, pady=10, padx=10)
        text_area2.insert(tk.INSERT, conjuntoSiguientes)
        text_area2.configure(state='disabled')

        text_area3.grid(column=0, row=5, pady=10, padx=10)
        text_area3.insert(tk.INSERT, conjuntoPrediccion)
        text_area3.configure(state='disabled')

        self.__generarTabla()
        self.ventanaResultado.mainloop()

    def __generarTabla(self, listaNoTerminales=['E', 'E\'', 'T', 'T\'', 'F'], listaTerminales=['+', '*', '(', ')', 'id']) -> None:

        treeview = ttk.Treeview(self.ventanaResultado,
                                columns=tuple(listaTerminales))
        treeview.grid(column=0, row=7)
        treeview.heading("#0", text="VT/VN")
        treeview.column("#0", width=50)
        count = 1
        for i in listaTerminales:
            treeview.heading("#{}".format(str(count)), text=i)
            treeview.column("#{}".format(str(count)), width=50)
            count = count + 1
        count = 1
        for j in listaNoTerminales:
            treeview.insert("", count, text=j)
            count = count + 1

# def __generarTabla(self) -> None:
#     lst = [(1, 'Raj', 'Mumbai', 19),
#            (2, 'Aaryan', 'Pune', 18),
#            (3, 'Vaishnavi', 'Mumbai', 20),
#            (4, 'Rachna', 'Mumbai', 21),
#            (5, 'Shubham', 'Delhi', 21)]

#     total_rows = len(lst)
#     total_columns = len(lst[0])
#     for i in range(total_rows):
#         for j in range(total_columns):
#             e = Entry(self.ventanaResultado, width=5, fg='blue')
#             e.grid(row=i, column=j)
#             e.insert(END, lst[i][j])
