from tkinter import *
from random import *
def Generar():
  
    if int(var1.get())>int(var2.get()):
        numeroG=str(randint(int(var2.get()),int(var1.get())))
        resultado.set(numeroG)
    elif int(var1.get())<int(var2.get()):
        numeroG=str(randint(int(var1.get()),int(var2.get())))
        resultado.set(numeroG)   



ventana = Tk()
ventana.title("GENERADOR DE NUMEROS")
ventana.geometry("500x300")
ventana.resizable(width=FALSE, height=FALSE)
ventana.config(bg="grey")

numero1=Label(ventana,text="Numero 1",font="arial,14",bg="grey")
numero1.place(x=130,y=70)
numero2=Label(ventana,text="Numero 2",font="arial,14",bg="grey")
numero2.place(x=130,y=130)

var1=StringVar()
var2=StringVar()

spin1=Spinbox(ventana,from_=0,to=100,width=10,textvariable=var1)
spin1.place(x=300,y=70)

spin2=Spinbox(ventana,from_=0,to=100,width=10,textvariable=var2)
spin2.place(x=300,y=130)

nrGen=Label(ventana,text=" Numero Generado ",font="arial,14",bg="grey", width=15)
nrGen.place(x=130,y=200)

resultado=StringVar()
n_generado=Label(ventana,textvariable=resultado,width=10,bg="white")
n_generado.place(x=300,y=200)

generar=Button(ventana,text="Generar",width=10,command=Generar)
generar.place(x=300,y=250)

ventana.mainloop()