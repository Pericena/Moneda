from tkinter import *
import random
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from Arbol import Arbol

import os
os.system('cmd /c "color a"')



def main():
    arbol = Arbol(3)
    '''
    print("Arbol Binario de Probabilidades :")
    arbol.paint_tree()
    '''
    print("----------------------------------")
    print("¿Cual es la posibilidad que una caiga dos veces cara en tres intentos?")
    a = arbol.probabilidad('Cara',2)
    b = arbol.cantidadnodoHoja()
    print (" Es la Cantidad de casos Favorables : "+str(a)+" dividido \n entre el total de todos los casos probables: "+str(b))
    print("respuesta: ",a/b)
    print("probabilidad:",a/b*100)
    print()


def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    

def producto():
    r.set( float(n1.get()) * float(n2.get()) )
    
def borrar():
    n1.set("")
    n2.set("")
    n3.set("")
    r.set("")
    string.set("")



def respuesta():
    arbol = Arbol(3) 
    a = arbol.probabilidad('Cara',2)
    b = arbol.cantidadnodoHoja()
    print("respuesta: ",a/b)
    #resp=(a/b)
    string= r.set(a/b)
    #print(resp)
    label.configure(text=string)
arbol = Arbol(3)
def probabilidad():
    a = arbol.probabilidad('Cara',2)
    b = arbol.cantidadnodoHoja()
    resp=(a/b)
    prob=(a/b*100)
    string= r.set(a/b*100)
    string1= r.set(a/b)
    print("respuesta: ",resp)
    print("probabilidad:",prob)
    label.configure(text=string)
    label.configure(text=string1)
    


   

# Configuración de la raíz
root = Tk()
root.title("Proyecto ED2")
counter = 0 
def conteo(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

def getvals():
    print("Datos :")

    print(f"{n3.get(), n1.get(), n2.get()} ")

    with open("records.txt", "a") as f:
        f.write(f"{n3.get(), n1.get(), n2.get()}\n ")

def coinFlip():
    result = np.random.binomial(1,0.5)
    tfield.delete("1.0", "end")
 
    if(result == 1):
        tfield.insert(INSERT, " Es ————> Cruz")
        i.config(image = heads)
         
    else:
        tfield.insert(INSERT, " ES ————> Cara")
        i.config(image = tails)

root.config(bd=15)
root.geometry("600x600")
Label(root,text="Juego de Moneda",fg = "red",font=("Courier 22 bold")).pack()
Label(root,text="ESTRUCTURA DE DATOS").pack()
Label(root,text="By Luishiño").pack()
#contador
label = Label(root, fg="green")
label.pack()
conteo(label)
#imagen cruz
load = Image.open("cruz.png")
heads = ImageTk.PhotoImage(load)
 
#imagen cara
load = Image.open("cara.png")
tails = ImageTk.PhotoImage(load)
 
i = Label(root, image=heads)
i.pack()

#Text mostrar si es cara o cruz
tfield = Text(root, width=50, height=2)
tfield.pack()
tfield.insert(INSERT, "Haga clic en el botón .. Para lanzar la moneda y obtener el resultado")

b1 = Button(root, text="Lanzar Moneda", font=("Arial", 10), command=coinFlip, bg='teal', fg='white', activebackground="lightblue", padx=10, pady=10)
b1.pack()

n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
r = StringVar()
string=StringVar()
string1=StringVar()
valor=StringVar()

#crear y iniciar label y input
Label(root, text="¿Cual es la posibilidad que una caiga dos veces cara en tres intentos?").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Probabilidad cruz").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Ingresar dato").pack()
Entry(root, justify="center", textvariable=n3).pack()

Label(root, text="Cantidad de intentos").pack()
Entry(root,justify="center",textvariable=r).pack()

Label(root, text="respuesta").pack()
Entry(root, justify="center", textvariable=r, state="disabled",font=("Courier 10 bold")).pack()

Label(root, text="Probabilidad").pack()
Entry(root, justify="center", textvariable=r, state="disabled",font=("Courier 10 bold")).pack()

Label(root, text="").pack()  # Separador

#Crear botones de acciones
Button(root, text="Sumar",justify="center",width=10, command=sumar).pack(side="left")
Button(root, text="Resta",justify="center",width=10, command=resta).pack(side="left")
Button(root, text="Producto",justify="center",width=10, command=producto).pack(side="left")
Button(text="Registrar",justify="center",width=10, command=getvals).pack(side="left")
Button(root, text= "Calcular",justify="center",width=10,command= probabilidad).pack(side="left")
Button(root, text='Borrar',justify="center", width=10, command=borrar).pack(side="left")
Button(root, text='Salir',justify="center", width=10, command=root.destroy).pack(side="left")
# Finalmente bucle de la aplicación

root.mainloop()

if __name__ == '__main__':
    main()