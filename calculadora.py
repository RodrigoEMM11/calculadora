from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Calculadora")
root.geometry("+500+80")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1)
label_entrada1.grid(column=0, row=0)

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2)
label_entrada2.grid(column=0, row=1)

button0 = ttk.Button(mainframe, text="0")
button1 = ttk.Button(mainframe, text="1")
button2 = ttk.Button(mainframe, text="2")
button3 = ttk.Button(mainframe, text="3")
button4 = ttk.Button(mainframe, text="4")
button5 = ttk.Button(mainframe, text="5")
button6 = ttk.Button(mainframe, text="6")
button7 = ttk.Button(mainframe, text="7")
button8 = ttk.Button(mainframe, text="8")
button9 = ttk.Button(mainframe, text="9")

button_borrar = ttk.Button(mainframe, text=chr(9003))
button_borrar_todo = ttk.Button(mainframe, text="C")
button_parentesis1 = ttk.Button(mainframe, text="(")
button_parentesis2 = ttk.Button(mainframe, text=")")
button_punto = ttk.Button(mainframe, text=".")

button_division = ttk.Button(mainframe, text=chr(247))
button_multiplicacion = ttk.Button(mainframe, text="x")
button_resta = ttk.Button(mainframe, text="-")
button_suma = ttk.Button(mainframe, text="+")

button_igual = ttk.Button(mainframe, text="=")
button_raiz = ttk.Button(mainframe, text="√")

#colocar botones en pantalla
button_parentesis1.grid(column=0, row=2)
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

root.mainloop()