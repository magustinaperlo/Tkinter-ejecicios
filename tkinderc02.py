from tkinter import *

def incrementar():
    valor=int (lbl_Valor["text"])
    lbl_Valor["text"]= f"{valor+1}"

contador=Tk()
contador.title("Contador creciente")

contador.rowconfigure(0,minsize=50,weight=1)
contador.columnconfigure ([0,1,2], minsize=50, weight=1)
ingreso= Entry(contador)
btn_incre=Button(contador, text="+",command=incrementar )
btn_incre.grid(row=0,column=2,sticky="nsew")
lbl_Valor= Label(contador,text="0")
lbl_Valor.grid(row=0,column=1)
etiqueta=Label(contador,text="contador")
etiqueta.grid(row=0,column=0)

contador.mainloop()
