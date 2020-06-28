from tkinter import *
from tkinter import ttk


def seven():
    entry_value.set(entry_value.get() + '7')

def eight():
    entry_value.set(entry_value.get() + '8')

def nine():
    entry_value.set(entry_value.get() + '9')

def zero():
    entry_value.set(entry_value.get() + '0')

def one():
    entry_value.set(entry_value.get() + '1')

def two():
    entry_value.set(entry_value.get() + '2')

def three():
    entry_value.set(entry_value.get() + '3')

def four():
    entry_value.set(entry_value.get() + '4')

def five():
    entry_value.set(entry_value.get() + '5')

def six():
    entry_value.set(entry_value.get() + '6')

def Minus():
    entry_value.set(entry_value.get() + '-')

def nanugi():
    entry_value.set(entry_value.get() + '/')

def gop():
    entry_value.set(entry_value.get() + '*')

def plus():
    entry_value.set(entry_value.get() + '+')

def Clear():
    entry_value.set('')

def Result():
    s = entry_value.get()
    answer = eval(s)
    entry_value.set(answer)

window = Tk()
window.title("Calculator")
# window.geometry("340x120")

entry_value = StringVar(window, value='')

number_entry = Entry(window, textvariable=entry_value, width=20, bg="yellow")
number_entry.grid(row=0, columnspan=3)

button7 = Button(window, text="7", command=seven, width=5)
button7.grid(row=3, column=0)
button8 = Button(window, text="8", command=eight, width=5)
button8.grid(row=3, column=1)
button9 = Button(window, text="9", command=nine, width=5)
button9.grid(row=3, column=2)
button_div = Button(window, text="/", command=nanugi, width=5)
button_div.grid(row=4, column=3)

button4 = Button(window, text="4", command=four, width=5)
button4.grid(row=2, column=0)
button5 = Button(window, text="5", command=five, width=5)
button5.grid(row=2, column=1)
button6 = Button(window, text="6", command=six, width=5)
button6.grid(row=2, column=2)
button_mult = Button(window, text="*", command=gop, width=5)
button_mult.grid(row=3, column=3)

button1 = Button(window, text="1", command=one, width=5)
button1.grid(row=1, column=0)
button2 = Button(window, text="2", command=two, width=5)
button2.grid(row=1, column=1)
button3 = Button(window, text="3", command=three, width=5)
button3.grid(row=1, column=2)
button_add = Button(window, text="+", command=plus, width=5)
button_add.grid(row=1, column=3)

button_ac = Button(window, text="C", command=Clear, width=5)
button_ac.grid(row=4, column=0)
button0 = Button(window, text="0", command=zero, width=5)
button0.grid(row=4, column=1)
button_equal = Button(window, text="=", command=Result, width=5)
button_equal.grid(row=4, column=2)
button_sub = Button(window, text="-", command=Minus, width=5)
button_sub.grid(row=2, column=3)

window.mainloop()