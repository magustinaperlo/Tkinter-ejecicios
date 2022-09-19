
from tkinter import *
import math

def calcular():
    res= n.get()+1
    resultado.config(text=math.factorial(res))
    for i in range(res):
        n.set(res)
    
    
Factorial=Tk()
Factorial.title("Factorial")
Factorial.rowconfigure([0,1,2],minsize=100,weight=1)
Factorial.columnconfigure([0,1,2,3,4],minsize=100,weight=1)

fact=Label(Factorial,text="n",bg="blue", width=5)
fact.grid(row=1,column=0)

n= IntVar(value=0)


box1=Entry(Factorial,textvariable=n,width=10,state="readonly")
box1.grid(row=1,column=1)

bt_sig=Button(Factorial,text="Siguiente",command=calcular)
bt_sig.grid(row=1,column=2)

etiqueta=Label(Factorial,text="El Factorial es",bg="lightblue")
etiqueta.grid(row=1,column=4)
res=IntVar()
resultado=Label(Factorial,text="1", width=10)
resultado.grid(row=1,column=5)



Factorial.mainloop()