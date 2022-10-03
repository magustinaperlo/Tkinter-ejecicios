from tkinter import *
from tkinter import messagebox

def sumar():
    suma= num1.get() + num2.get()
    return res.set(suma)
def restar():
    resta= num1.get() - num2.get()
    return res.set(resta)
def porcentaje():
    por= num1.get() * num2.get()/100
    return res.set(por)
def multiplicar():
    mult= num1.get() * num2.get()
    return res.set(mult)
def dividir():
    if num2.get()==0:
        messagebox.showwarning("Error","No se puede dividir por 0")
    else:
        div= num1.get() / num2.get()
        return res.set(div)
    
def clear():
    clear=""
    return num1.set(clear), num2.set(clear),res.set(clear)                 
ventana=Tk()
ventana.title("CALCULADORA")

ventana.rowconfigure([0,1,2,3,4,5],minsize=50,weight=1)
ventana.columnconfigure ([0,1], minsize=50, weight=1)
ventana.config(bg="lightblue")

et1=Label(ventana,text="Primer Numero",bg="lightblue").grid(row=0,column=0)
et2=Label(ventana,text="Segundo Numero",bg="lightblue").grid(row=1,column=0)
et3=Label(ventana,text="Resultado",bg="lightblue").grid(row=2,column=0)

num1=DoubleVar()
numero1=Entry(ventana, textvariable=num1,width=10).grid(row=0,column=1)
num2=DoubleVar()
numero2=Entry(ventana, textvariable=num2,width=10).grid(row=1,column=1)
res=DoubleVar()
resultado=Entry(ventana, textvariable=res,width=10,state="disabled").grid(row=2,column=1)

btmas=Button(ventana,text="+",width=10,command=sumar).grid(row=3,column=0)
btmult=Button(ventana,text="*",width=10,command=multiplicar).grid(row=4,column=0)
btpje=Button(ventana,text="%",width=10,command=porcentaje).grid(row=5,column=0)
btmen=Button(ventana,text="-",width=10,command=restar).grid(row=3,column=1)
btdiv=Button(ventana,text="/",width=10,command=dividir).grid(row=4,column=1)
btclear=Button(ventana,text="CLEAR",width=10,command=clear).grid(row=5,column=1)

ventana.mainloop()
