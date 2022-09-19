
from tkinter import *

def incrementar():
    valor=int (lbl_Valor["text"])
    lbl_Valor["text"]= f"{valor+1}"
    
def decrementar():
    valor=int (lbl_Valor["text"])
    lbl_Valor["text"]= f"{valor-1}"

def clear():
    valor=int (lbl_Valor["text"])
    lbl_Valor["text"]= 0

ventana=Tk()
ventana.title("Contador")
#ventana.iconbitmap("Masked.ico")
ventana.rowconfigure(0,minsize=50,weight=1)
ventana.columnconfigure ([0,1,2,3,4], minsize=50, weight=1)

contador=Label(ventana, text="Contador")
contador.grid(row=0,column=0)
btn_decre=Button(ventana, text="Count Down",command=decrementar)#llamamos al metodo boton decrementar, que tenga el texto - yel metodo comand llama a la funcion
btn_decre.grid(row=0,column=3,sticky="nsew")#Le decimos que sea visible con el metodo grid

lbl_Valor= Label(ventana,text="0")
lbl_Valor.grid(row=0,column=1)

btn_incre=Button(ventana, text="Count Up",command=incrementar)#llamamos al metodo boton decrementar, que tenga el texto +
btn_incre.grid(row=0,column=2,sticky="nsew")#Le decimos que sea visible con el metodo grid
btn_clear= Button(ventana, text="Reset",command=clear)
btn_clear.grid(row=0,column=4,sticky="nsew")


ventana.mainloop()