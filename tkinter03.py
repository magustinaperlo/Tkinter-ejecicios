
from tkinter import *
import tkinter

def decrementar():
    valor= int(ingreso.get()) -1
    num.set(valor)

contador=Tk()
contador.title("Contador decreciente")


contador.rowconfigure(0,minsize=50,weight=1)
contador.columnconfigure ([0,1,2,], minsize=50, weight=1)

num=tkinter.IntVar()

ingreso=tkinter.Entry(contador,text=num,state="readonly",width=5)

ingreso.grid(row=0,column=1)

btn_incre=Button(contador, text="-",command=decrementar,font=("", 12))
btn_incre.grid(row=0,column=2,sticky="nsew")

etiqueta=Label(contador,text="Contador",font=("arial",10))
etiqueta.grid(row=0,column=0)
num.set("88")
contador.mainloop()
