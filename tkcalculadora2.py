from tkinter import *
from select import select
from multiprocessing.sharedctypes import Value
from tkinter import messagebox


def calcular():
    
    op=opcion.get()
    
    if op==1:
        suma= num1.get() + num2.get()
        return res.set(suma)
    
    if op==2:
        resta= num1.get() - num2.get()
        return res.set(resta)
    
    if op==3:
        mult= num1.get() * num2.get()
        return res.set(mult)
   
    if op==4:
        if num2.get()==0:
            messagebox.showwarning("Error","No se puede dividir por 0")
        else:
            div= num1.get() / num2.get()
        return res.set(div)
    
    
ventana=Tk()
ventana.title("CALCULADORA")

ventana.rowconfigure([0,1,2,3,4,5,6],minsize=50,weight=1)
ventana.columnconfigure ([0,1,2], minsize=50, weight=1)
ventana.config(bg="lightblue")

v1_label=Label(ventana,text="Valor 1")
v1_label.grid(row=1,column=0)

v2_label=Label(ventana,text="Valor 2")
v2_label.grid(row=2,column=0)

v3_label=Label(ventana,text="Resultado")
v3_label.grid(row=3,column=0)
num1=DoubleVar()
num2=DoubleVar()
res=DoubleVar()
# num1=IntVar()
# num2=IntVar()
# res=IntVar()
opcion=IntVar()

box1=Entry(ventana,textvariable=num1,width=10)
box1.grid(row=1,column=1)

box2=Entry(ventana,textvariable=num2,width=10)
box2.grid(row=2,column=1)

box3=Entry(ventana,textvariable=res,width=10)
box3.grid(row=3,column=1)

op_label=Label(ventana,text="Operaciones")
op_label.grid(row=0,column=3)

btn_calcular=Button(ventana,text="Calcular",command=calcular)
btn_calcular.grid(row=4,column=1)

psum=Radiobutton(ventana,text="Sumar",value=1,variable=opcion,bg="lightblue",justify="center")
psum.grid(row=1,column=3)

pres=Radiobutton(ventana,text="Restar",value=2,variable=opcion,bg="lightblue",justify="right")
pres.grid(row=2,column=3)

pmul=Radiobutton(ventana,text="Multiplicar",value=3,variable=opcion,bg="lightblue",justify="right")
pmul.grid(row=3,column=3)

pdiv=Radiobutton(ventana,text="Dividir",value=4,variable=opcion,bg="lightblue",justify="right")
pdiv.grid(row=4,column=3)

ventana.mainloop()
