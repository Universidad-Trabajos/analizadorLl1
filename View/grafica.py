import tkinter as tk


class Grafica:
    anchoVentana = 700
    altoVentana = 980

    def __init__(self):
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
        entry = tk.Entry(self.ventana)
        entry.pack()

        l2 = tk.Label(self.ventana, text="Ingrese los terminales: ")
        l2.pack()
        entry2 = tk.Entry(self.ventana)
        entry2.pack()

        l3 = tk.Label(self.ventana, text="Ingrese las producciones: ")
        l3.pack()
        entry3 = tk.Text(self.ventana)
        entry3.pack(padx=280)

        button = tk.Button(self.ventana, text="Generar Análisis",
                           bg="light blue", borderwidth=5)
        button.pack()
