from tkinter import *

from setuptools import Command

ventana = Tk()

ventana.grid()
boton=Button(text="Hola",width=10,height=10)
boton.grid(column=0,row=0)
boton.config(command=lambda:print("hola"))
boton.pack()
ventana.mainloop()