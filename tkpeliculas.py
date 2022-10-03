
from tkinter import *
from tkinter import messagebox

def limpiar():
    nombre.set("")

# def agregar():
#     lista.insert(END,nombre.get())
#     limpiar()

def agregar():
    a = nombre.get() #Se obtiene valor en Entry
   #validamos el ingreso para no almacenar datos erróneos
    if (a.isspace() or len(a) <= 1):
        messagebox.showinfo(message="El nombre de la película no debe comenzar con un espacio", title="Error")
        limpiar()
    else:
        lista.insert(END, a) #Se inserta en Listbox
        limpiar()


    
ventana=Tk()
ventana.title("PELICULAS")

ventana.rowconfigure([0,1,2],minsize=50,weight=1)
ventana.columnconfigure ([0,1], minsize=50, weight=1)
#se añaden valores fijos para la dimensión de la ventana
ventana.minsize(500,400)
ventana.maxsize(500,400)
ventana.config(bg="lightgreen")

et1=Label(ventana,text="Escribe un titulo de Pelicula",bg="pink").grid(row=0,column=0)
et2=Label(ventana,text="Películas",bg="pink").grid(row=1,column=1)
nombre=StringVar()
box=Entry(ventana,textvariable=nombre,width=30).grid(row=1,column=0,ipadx=1)

btn=Button(ventana,text="Agregar",command=agregar).grid(row=2,column=0)

lista=Listbox(ventana,width=30)
lista.grid(row=2,column=1)
barra = Scrollbar(ventana, command= Listbox.yview,).grid(row=2,column=2) #no funciona
ventana.mainloop()
