import tkinter
from tkinter import *
import math

'''variable to store past results'''
key_information = {'Operation': "", "First Number": None}

'''setting up the GUI settings'''
root = Tk()
root.title("Simple Calculator")
root.geometry("630x460")


'''The Entry box for the Number'''
e: Entry = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=3, columnspan=10,padx=10,pady=20)


'''Space in-between numbers and operations'''
space1 = Label(root, text="")
space1.grid(row=1,column=2, padx=50)

'''all functionality for buttons 0 through 9'''
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

Button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

Button_1.grid(row=3, column=3)
Button_2.grid(row=3, column=4)
Button_3.grid(row=3, column=5)
Button_4.grid(row=2, column=3)
Button_5.grid(row=2, column=4)
Button_6.grid(row=2, column=5)
Button_7.grid(row=1, column=3)
Button_8.grid(row=1, column=4)
Button_9.grid(row=1, column=5)
Button_0.grid(row=4, column=3)


'''functionality for the clear and equal buttons'''
def button_clear():
    e.delete(0, END)


def button_equal(key_information):
    try:
        second_number = e.get()
        e.delete(0, END)
        if key_information['Operation'] == "+":
            e.insert(0, float(key_information['First Number']) + float(second_number))
        if key_information['Operation'] == "*":
            e.insert(0, float(key_information['First Number']) * float(second_number))
        if key_information['Operation'] == "/":
            e.insert(0, float(key_information['First Number']) / float(second_number))
        if key_information['Operation'] == "-":
            e.insert(0, float(key_information['First Number']) - float(second_number))
        if key_information['Operation'] == "1/":
            e.insert(0, 1 / float(key_information['First Number']))
        if key_information['Operation'] == "sqrt":
            e.insert(0, math.sqrt(float(key_information['First Number'])))
        if key_information['Operation'] == "sq":
            e.insert(0, math.pow(float(key_information['First Number']),2))
        if key_information['Operation'] == "%":
            e.insert(0, float(key_information['First Number']) % float(second_number))
        if key_information['Operation'] == "factorial":
            e.insert(0, math.factorial(int(key_information['First Number'])))
        if key_information['Operation'] == "log":
            e.insert(0, math.log(float(key_information['First Number']), float(second_number)))
        if key_information['Operation'] == "nth_pow":
            e.insert(0, math.pow(float(key_information['First Number']), float(second_number)))
        if key_information['Operation'] == "nth_root":
            e.insert(0, float(key_information['First Number'])** (1 / float(second_number)))
    except:
        pass
Button_equal = Button(root, text="=", padx=89, pady=20, command=lambda: button_equal(key_information))
Button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_clear())

Button_clear.grid(row=4, column=4, columnspan=2)
Button_equal.grid(row=5, column=4, columnspan=2)


'''functionality for the first four basic functions: divide, multiply, subtract and add'''
def button_divide(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "/"
    e.delete(0, END)

def button_multiply(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "*"
    e.delete(0, END)

def button_subtract(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "-"
    e.delete(0, END)

def button_add(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "+"
    e.delete(0, END)

Button_divide = Button(root, text=" / ", padx=40,pady=20, command=lambda: button_divide(key_information))
Button_add = Button(root, text=" + ", padx=40, pady=20, command=lambda: button_add(key_information))
Button_subtract = Button(root, text= " - ", padx=40,pady=20, command=lambda: button_subtract(key_information))
Button_multiply = Button(root, text=" * ", padx=40,pady=20, command=lambda: button_multiply(key_information))

Button_divide.grid(row=1, column=0)
Button_multiply.grid(row=1, column=1, sticky="w")
Button_subtract.grid(row=2,column=0)
Button_add.grid(row=2,column=1, sticky="w")

'''Everything Above is correct ^^'''
'''functionality for the four intermediate operations, reciporcal (recip), sqrt, sq (square), modulo (%)'''
def button_recip(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "1/"
    e.delete(0, END)


def button_sqrt(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "sqrt"
    e.delete(0, END)

def button_sq(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "sq"
    e.delete(0, END)

def button_modulo(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "%"
    e.delete(0, END)

reciporcal_button = Button(root, text="Reciporcal", padx=20,pady=20, command=lambda: button_recip(key_information))
sqrt_button = Button(root, text="SQRT", padx=33,pady=20, command=lambda: button_sqrt(key_information))
square_button = Button(root, text="SQUARE", padx=25,pady=20, command=lambda: button_sq(key_information))
modulo_button = Button(root, text="MODULO", padx=25,pady=20, command=lambda: button_modulo(key_information))

reciporcal_button.grid(row=3, column=0)
sqrt_button.grid(row=3, column=1)
modulo_button.grid(row=4, column=0)
square_button.grid(row=4, column=1)



'''functionality for the last four advanced operations: fact (factorial), log, Nth root, Nth power'''

def button_fact(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "factorial"
    e.delete(0, END)


def button_log(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "log"
    e.delete(0, END)


def button_nth_root(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "nth_root"
    e.delete(0, END)

def button_nth_power(key_information):
    key_information['First Number'] = float(e.get())
    key_information['Operation'] = "nth_pow"
    e.delete(0, END)

factorial_button = Button(root, text="!", padx=45,pady=20, command=lambda: button_fact(key_information))
log_button = Button(root, text="log", padx=40,pady=20, command=lambda: button_log(key_information))
nth_root_button = Button(root, text="Nth root", padx=25,pady=20, command=lambda: button_nth_root(key_information))
nth_power_button = Button(root, text="Nth pow", padx=25,pady=20, command=lambda: button_nth_power(key_information))

factorial_button.grid(row=5, column=0)
log_button.grid(row=5, column=1)
nth_power_button.grid(row=6, column=0)
nth_root_button.grid(row=6, column=1)


root.mainloop()
