from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Arbol import Arbol


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Proyecto ED2")
        self.ventana1.geometry("400x380")

        self.label11=tk.Label(self.ventana1,text="Juego de Moneda",fg = "green",font=("Courier 22 bold"))
        self.label11.grid(column=1, row=3)

        self.label15=tk.Label(self.ventana1,text="ESTRUCTURA DE DATOS",fg = "black",font=("Courier 10 bold"))
        self.label15.grid(column=1, row=4)
        self.label14=tk.Label(self.ventana1,text="By Luishiño",fg = "black",font=("Courier 8 bold"))
        self.label14.grid(column=1, row=5)
        
        self.label13=tk.Label(self.ventana1,text="¿Cual es la posibilidad que una caiga dos veces cara en tres intentos?",fg='red')
        self.label13.grid(column=1, row=6)

        self.label1=tk.Label(self.ventana1,text="Ingrese un número:")
        self.label1.grid(column=1, row=7)
        self.dato=tk.StringVar()
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=8, textvariable=self.dato1, font=("Arial", 15), fg='black')
        self.entry1.grid(column=1, row=10)
        self.entry2=tk.Entry(self.ventana1, width=8, textvariable=self.dato, font=("Arial", 15), fg='red')
        self.entry2.grid(column=1, row=11)
        self.boton1=tk.Button(self.ventana1, text="Calcular",justify="center", font=("Arial", 8), command=self.probabilidad, bg='teal', fg='white', activebackground="lightblue", padx=4, pady=4)
        self.boton1.grid(column=1, row=12)
        self.label2=tk.Label(self.ventana1,text="resultado", font=("Arial", 15), fg='Green')
        self.label2.grid(column=1, row=14)
        
        self.boton2=tk.Button(self.ventana1, text='Salir',justify="left", width=10, command=self.ventana1.destroy,fg='white', activebackground="red",bg='red')
        self.boton2.grid(column=1, row=16)

        #Text mostrar si es cara o cruz
        self.load = Image.open("cruz.png")
        self.heads = ImageTk.PhotoImage(self.load)
        self.i = Label(self.ventana1, image=self.heads)
        self.i.grid(column=1, row=0)
        self.load = Image.open("cara.png")
        self.tails = ImageTk.PhotoImage(self.load)
        self.i = tk.Label(self.ventana1, image=self.tails)
        self.i.grid(column=1, row=0)
       
        self.ventana1.mainloop()


        
    def probabilidad(self):
        arbol = Arbol(int(self.dato.get()))
        a = arbol.probabilidad('Cara',(int(self.dato1.get())))
        #a=arbol.probabilidad('Cara',2)
        b = arbol.cantidadnodoHoja()
        respuesta=(a/b)
        probabilidad=(a/b*100)
        print (" Es la Cantidad de casos Favorables : "+str(a)+" dividido \n entre el total de todos los casos probables: "+str(b))
        print("respuesta: ",a/b)
        print("probabilidad:",a/b*100)
        
        self.label2.configure(text=respuesta)
        self.label2.configure(text=probabilidad)

aplicacion1=Aplicacion()   


