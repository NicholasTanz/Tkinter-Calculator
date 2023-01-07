import tkinter
from tkinter import *
import math
'''2nd Version I made a while back'''
'''variable to store past results'''
past_results = {}
counter=0

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
    past_results.clear()


def button_equal():
    second_number = e.get()
    global counter
    e.delete(0, END)
    if op == "+":
        e.insert(0, f_num + float(second_number))
        past_results[counter] = str(f_num) + " + " + str(second_number) + " = " + str(f_num + float(second_number))
    if op == "*":
        e.insert(0, f_num * float(second_number))
        past_results[counter] = str(f_num) + " * " + str(second_number) + " = " + str(f_num * float(second_number))
    if op == "/":
        e.insert(0, f_num / float(second_number))
        past_results[counter] = str(f_num) + " / " + str(second_number) + " = " + str(f_num / float(second_number))
    if op == "-":
        e.insert(0, float(f_num) - float(second_number))
        past_results[counter] = str(f_num) + " - " + str(second_number) + " = " + str(f_num - float(second_number))
    if op == "%":
        e.insert(0, f_num % float(second_number))
        past_results[counter] = str(f_num) + " % " + str(second_number) + " = " + str(f_num % float(second_number))
    if op == "nth_root":
        e.insert(0, f_num**(1/float(second_number)))
        past_results[counter] = str(f_num) + " ^1/ " + str(second_number) + " = " + str((f_num ** (1/float(second_number))))
    if op == "nth_power":
        e.insert(0, str(pow(f_num, int(second_number))))
        past_results[counter] = str(f_num) + " ** " + str(second_number) + " = " + str(f_num ** float(second_number))
    counter+=1

Button_equal = Button(root, text="=", padx=89, pady=20, command=lambda: button_equal())
Button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_clear())

Button_clear.grid(row=4, column=4, columnspan=2)
Button_equal.grid(row=5, column=4, columnspan=2)


'''functionality for the first four basic functions: divide, multiply, subtract and add'''
def button_divide():
    global f_num
    global op
    f_num = float(e.get())
    op = "/"
    e.delete(0, END)

def button_multiply():
    global f_num
    global op
    f_num = float(e.get())
    op = "*"
    e.delete(0, END)

def button_subtract():
    global f_num
    global op
    f_num = float(e.get())
    op = "-"
    e.delete(0, END)

def button_add():
    global f_num
    global op
    f_num = float(e.get())
    op = "+"
    e.delete(0, END)

Button_divide = Button(root, text=" / ", padx=40,pady=20, command=lambda: button_divide())
Button_add = Button(root, text=" + ", padx=40, pady=20, command=lambda: button_add())
Button_subtract = Button(root, text= " - ", padx=40,pady=20, command=lambda: button_subtract())
Button_multiply = Button(root, text=" * ", padx=40,pady=20, command=lambda: button_multiply())

Button_divide.grid(row=1, column=0)
Button_multiply.grid(row=1, column=1, sticky="w")
Button_subtract.grid(row=2,column=0)
Button_add.grid(row=2,column=1, sticky="w")

'''functionality for the four intermediate operations, reciporcal (recip), sqrt, sq (square), modulo (%)'''
def button_recip():
    global f_num
    global op
    global counter
    op = "recip"
    f_num = float(e.get())
    e.delete(0, END)
    e.insert(0, str(1 / f_num))
    past_results[counter] = "1 / " + str(f_num) + " = " + str((1/float(f_num)))
    counter+=1

def button_sqrt():
    global f_num
    global op
    global counter
    op = "sqrt"
    f_num = float(e.get())
    e.delete(0, END)
    e.insert(0, str(math.sqrt(f_num)))
    past_results[counter] = "sqrt(" + str(f_num) + ") = " + str(math.sqrt(f_num))
    counter+=1

def button_sq():
    global f_num
    global op
    global counter
    op = "sq"
    f_num = float(e.get())
    e.delete(0, END)
    e.insert(0, str(pow(f_num, 2)))
    past_results[counter] = str(f_num) + "*" + str(f_num) + "=" + str(f_num * f_num)
    counter+=1

def button_modulo():
    global f_num
    global op
    f_num = float(e.get())
    op = "%"
    e.delete(0, END)

reciporcal_button = Button(root, text="Reciporcal", padx=20,pady=20, command=lambda: button_recip())
sqrt_button = Button(root, text="SQRT", padx=33,pady=20, command=lambda: button_sqrt())
square_button = Button(root, text="SQUARE", padx=25,pady=20, command=lambda: button_sq())
modulo_button = Button(root, text="MODULO", padx=25,pady=20, command=lambda: button_modulo())

reciporcal_button.grid(row=3, column=0)
sqrt_button.grid(row=3, column=1)
modulo_button.grid(row=4, column=0)
square_button.grid(row=4, column=1)


'''functionality for the last four advanced operations: fact (factorial), log, Nth root, Nth power'''
def button_fact():
    global f_num
    global op
    global counter
    f_num = int(float((e.get())))
    fact = 1
    for i in range(1, f_num + 1):
        fact *=i
    e.delete(0, END)
    e.insert(0, str(fact))
    past_results[counter] = str(f_num) + " * " + str(f_num - 1) + " * " + str(f_num - 2) + " * " + str(f_num - 3) + "..." + " = " + str(fact)
    counter+=1


def button_log():
    global f_num
    global op
    global counter
    f_num = float(e.get())
    e.delete(0, END)
    e.insert(0, str(math.log(f_num, 10)))
    past_results[counter] = "log(" + str(f_num) + ") =" + str(math.log(f_num, 10))
    counter+=1

def button_nth_root():
    global f_num
    global op
    f_num = float(e.get())
    e.delete(0, END)
    op = "nth_root"

def button_nth_power():
    global f_num
    global op
    f_num = float(e.get())
    e.delete(0, END)
    op = "nth_power"

factorial_button = Button(root, text="!", padx=45,pady=20, command=lambda: button_fact())
log_button = Button(root, text="log", padx=40,pady=20, command=lambda: button_log())
nth_root_button = Button(root, text="Nth root", padx=25,pady=20, command=lambda: button_nth_root())
nth_power_button = Button(root, text="Nth pow", padx=25,pady=20, command=lambda: button_nth_power())

factorial_button.grid(row=5, column=0)
log_button.grid(row=5, column=1)
nth_power_button.grid(row=6, column=0)
nth_root_button.grid(row=6, column=1)

'''Functionality for a History button that displays the last five calculations'''

def btn_results():
    results_page = Tk()
    results_page.title("Last Five Calculations: ")
    results_page.geometry("600x600")
    def exit_btn():
        results_page.destroy()
        results_page.quit()

    def last_five_calcs():
        if len(past_results) < 5:
            past_results_list = []
            for i in range(0, len(past_results)):
                past_results_list.append(past_results[i])
            return past_results_list
        else:
            len_results = len(past_results)
            past_results_list = []
            for i in range(len(past_results) - 5, len(past_results)):
                past_results_list.append(past_results[i])
            return past_results_list

    exit_btnw = Button(results_page, text="exit",padx=20,pady=20, command=lambda:exit_btn())
    exit_btnw.grid(row=0,column=0)

    last_five = last_five_calcs()
    if len(last_five) == 5:
        label_results = Label(results_page, text=str(last_five[4]) + "\n" + str(last_five[3])
                          + "\n" + str(last_five[2]) + "\n" + str(last_five[1]) + "\n" +
                          str(last_five[0] + "\n"))
    elif len(last_five) == 4:
        label_results = Label(results_page, text=str(last_five[3]) + "\n" + str(last_five[2])
                          + "\n" + str(last_five[1]) + "\n" + str(last_five[0]) + "\n"
                          )
    elif len(last_five) == 3:
        label_results = Label(results_page, text=str(last_five[2])
                          + "\n" + str(last_five[1]) + "\n" + str(last_five[0]) + "\n"
                          )
    elif len(last_five) == 2:
        label_results = Label(results_page, text=str(last_five[1]) + "\n" + str(last_five[0]) + "\n"
                          )
    elif len(last_five) == 1:
        label_results = Label(results_page, text=str(last_five[0]) + "\n"
                          )
    else:
        label_results = Label(results_page, text="No results to display")
    label_results.grid(row=1,column=0)

    results_page.mainloop()



results_btn = Button(root, text="History",padx=22,pady=20, command=lambda:btn_results())

results_btn.grid(row=4,column=3)



root.mainloop()
