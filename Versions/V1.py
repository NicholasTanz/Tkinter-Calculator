'''This was created a few years back''' 
import tkinter
from tkinter import *
import math
from math import *


C1 = Tk()
C1.title("BasicCalculator")

value_enter = Entry(C1, borderwidth=5, width=10)
value_enter.grid(column=0,row=0, columnspan=10)

def squarert():
    global first_num
    first_num = value_enter.get()
    value_enter.delete(0, END)
    squarert_num = math.sqrt(float(first_num))
    value_enter.insert(0, str(squarert_num))

def multiply1():
    global first_num
    first_num = value_enter.get()
    value_enter.delete(0, END)

def square1():
    global first_num
    first_num = value_enter.get()
    value_enter.delete(0, END)
    square_num = float(first_num) * float(first_num)
    value_enter.insert(0, str(square_num))

def recip1():
    global first_num
    first_num = value_enter.get()
    value_enter.delete(0, END)
    reciporcal_VAL = 1 / float(first_num)
    value_enter.insert(0, reciporcal_VAL)

def clear():
    value_enter.delete(0, END)


def equal1():
    global second_num
    second_num = value_enter.get()
    value_enter.delete(0, END)
    total_multi = float(first_num) * float(second_num)
    value_enter.insert(0, str(total_multi))

sqrt = Button(C1, padx=25,pady=25,text="sqrt", command=lambda:squarert())
multiply = Button(C1, padx=25,pady=25,text="*", command=lambda:multiply1())
square = Button(C1, padx=25,pady=25,text="x^2", command=lambda:square1())
equal = Button(C1, padx=25,pady=25,text="=", command=lambda:equal1())
recpiorcal = Button(C1, padx=25,pady=25, text="recip", command=lambda:recip1())
clear1 = Button(C1, padx=25,pady=25,text="clear", command=lambda:clear())

clear1.grid(row=2,column=2)
recpiorcal.grid(row=1,column=2)
sqrt.grid(row=1,column=0)
multiply.grid(row=1,column=1)
square.grid(row=2,column=0)
equal.grid(row=2,column=1)





C1.mainloop()
