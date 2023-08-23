from interfaz import *
from tkinter import *
from tkinter import ttk
import math

def ingresarValores(tecla):
    if tecla >= 0 and tecla <= 9 or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)